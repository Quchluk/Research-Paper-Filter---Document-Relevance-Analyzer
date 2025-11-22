import os
import csv
from pathlib import Path
from dotenv import load_dotenv
import requests
import json
from prompt import SYSTEM_PROMPT, SYSTEM_PROMPT_RETRY, USER_PROMPT_TEMPLATE, USER_PROMPT_RETRY_TEMPLATE

# Load environment variables (force reload)
load_dotenv(override=True)

def query_grok(document_text, retry=False):
    """
    Determine if discusses Soviet Union in the Middle East or Lebanon 
    Returns: 1 (relevant), 0 (not relevant), or None (invalid response)
    """
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in .env file")
    
    # Limit document text to avoid token limits
    doc_text = document_text[:3000]
    
    # Construct the prompt
    if retry:
        system_prompt = SYSTEM_PROMPT_RETRY
        user_prompt = USER_PROMPT_RETRY_TEMPLATE.format(document_text=doc_text)
    else:
        system_prompt = SYSTEM_PROMPT
        user_prompt = USER_PROMPT_TEMPLATE.format(document_text=doc_text)
    
    # Make request to OpenRouter
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-v3.2-exp",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.0,  # More deterministic
                "max_tokens": 10  # We only need 1 character
            },
            timeout=30
        )
        
        if response.status_code != 200:
            print(f"API Error - Status: {response.status_code}")
            print(f"Response: {response.text}")
            response.raise_for_status()
        
        result = response.json()
        
        # Extract the response
        answer = result['choices'][0]['message']['content'].strip()
        
        # Validate response
        if answer == '1':
            return 1
        elif answer == '0':
            return 0
        else:
            print(f"Invalid response: '{answer}'")
            return None
            
    except Exception as e:
        print(f"Error querying Grok: {e}")
        return None

def main():
    # Path to OCR text files (relative to script location)
    script_dir = Path(__file__).parent.resolve()
    db_path = script_dir / "db"

    if not db_path.exists():
        print(f"Error: Directory not found at {db_path}")
        return
    
    # Get all OCR text files
    txt_files = list(db_path.glob("*_ocr.txt"))
    
    if not txt_files:
        print(f"No OCR text files found in {db_path}")
        return
    
    print(f"Found {len(txt_files)} OCR text files to analyze.")
    print("="*60)
    
    results = []
    
    for i, txt_file in enumerate(txt_files, 1):
        print(f"\nProcessing file {i}/{len(txt_files)}: {txt_file.name}", flush=True)
        
        try:
            # Read the document text
            with open(txt_file, 'r', encoding='utf-8') as f:
                document_text = f.read()
            
            # Query Grok
            relevance = query_grok(document_text)
            
            # Retry if invalid response
            if relevance is None:
                print("  Retrying with stricter prompt...")
                relevance = query_grok(document_text, retry=True)
            
            # If still invalid, mark as error
            if relevance is None:
                print(f"  [!] Failed to get valid response")
                relevance = -1  # Use -1 to indicate error
            else:
                status = "RELEVANT" if relevance == 1 else "NOT RELEVANT"
                print(f"  [{relevance}] {status}")
            
            results.append({
                'filename': txt_file.name,
                'relevant': relevance
            })
            
        except Exception as e:
            print(f"  [X] Error processing file: {e}")
            results.append({
                'filename': txt_file.name,
                'relevant': -1
            })
    
    # Save results to CSV
    output_file = script_dir / "relevance_results.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['filename', 'relevant'])
        writer.writeheader()
        writer.writerows(results)
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    
    # Summary
    relevant_count = sum(1 for r in results if r['relevant'] == 1)
    not_relevant_count = sum(1 for r in results if r['relevant'] == 0)
    error_count = sum(1 for r in results if r['relevant'] == -1)
    
    print(f"Relevant documents: {relevant_count}")
    print(f"Not relevant documents: {not_relevant_count}")
    print(f"Errors: {error_count}")
    print(f"\nResults saved to: {output_file}")
    print("="*60)

if __name__ == "__main__":
    main()

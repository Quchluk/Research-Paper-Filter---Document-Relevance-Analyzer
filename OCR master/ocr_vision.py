import os
import io
from pathlib import Path
from google.cloud import vision
from pdf2image import convert_from_path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def ocr_pdf_with_vision(pdf_path):
    """Extract text from PDF using Google Cloud Vision API"""

    # Set credentials from environment
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set in .env file")

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    # Initialize Vision API client
    client = vision.ImageAnnotatorClient()

    # Poppler path (local installation)
    POPPLER_PATH = Path(__file__).parent / "poppler" / "poppler-24.02.0" / "Library" / "bin"

    # Convert PDF to images
    print(f"Converting PDF to images: {pdf_path}")
    try:
        # Pass poppler_path explicitly
        images = convert_from_path(pdf_path, poppler_path=str(POPPLER_PATH))
        print(f"Successfully converted {len(images)} pages")
    except Exception as e:
        print(f"Error converting PDF: {e}")
        print(f"Poppler path checked: {POPPLER_PATH}")
        print("Make sure poppler is installed correctly in the 'poppler' subdirectory.")
        raise

    all_text = []

    # Process each page
    for i, image in enumerate(images, 1):
        print(f"Processing page {i}/{len(images)}...")

        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Create Vision API image object
        vision_image = vision.Image(content=img_byte_arr)

        # Perform text detection
        response = client.text_detection(image=vision_image)
        texts = response.text_annotations

        if texts:
            page_text = texts[0].description
            all_text.append(f"\n{'='*60}\n Page {i}\n{'='*60}\n{page_text}")
        else:
            all_text.append(f"\n{'='*60}\n Page {i}\n{'='*60}\n[No text detected]")

        # Check for errors
        if response.error.message:
            raise Exception(f'Vision API Error: {response.error.message}')

    return '\n'.join(all_text)

def main():
    # Input directory path - relative to script location
    script_dir = Path(__file__).parent.resolve()
    db_path = script_dir / "OCR  imput output"

    # Verify directory exists
    if not db_path.exists():
        print(f"Error: Directory not found at {db_path}")
        return

    # Get all PDF files
    pdf_files = list(db_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {db_path}")
        return

    print(f"Found {len(pdf_files)} PDF files to process.")
    print("="*60)

    success_count = 0
    error_count = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        try:
            print(f"\nProcessing file {i}/{len(pdf_files)}: {pdf_path.name}")
            print("-" * 40)
            
            extracted_text = ocr_pdf_with_vision(str(pdf_path))

            # Save to file
            output_path = pdf_path.with_name(f"{pdf_path.stem}_ocr.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)

            print(f"[V] Saved to: {output_path.name}")
            success_count += 1

        except Exception as e:
            print(f"[X] Error processing {pdf_path.name}: {str(e)}")
            error_count += 1
            # Continue to next file instead of stopping
            continue

    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)
    print(f"Successfully processed: {success_count}")
    print(f"Errors: {error_count}")
    print("="*60)

if __name__ == "__main__":
    main()

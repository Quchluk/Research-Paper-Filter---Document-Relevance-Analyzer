# Quick Start Guide

This guide will help you get the Research Paper Filter system up and running quickly.

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.8 or higher installed
- [ ] pip package manager
- [ ] Google Cloud Platform account
- [ ] OpenRouter account
- [ ] Basic familiarity with command line/terminal

## Installation Steps

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd "Data extractor/OCR master"
```

### 2. Create Virtual Environment (Recommended)

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Google Cloud Vision API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Cloud Vision API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Cloud Vision API"
   - Click "Enable"
4. Create service account credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Download the JSON key file
   - Save it securely (e.g., in your home directory)

### 5. Set Up OpenRouter API

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for an account
3. Navigate to [API Keys](https://openrouter.ai/keys)
4. Generate a new API key
5. Copy the key (you won't be able to see it again)

### 6. Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` file with your actual credentials:
```env
GOOGLE_APPLICATION_CREDENTIALS=/Users/yourname/path/to/credentials.json
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxx
```

### 7. Install Poppler

**macOS:**
```bash
brew install poppler
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install poppler-utils
```

**Windows:**
- Download from: https://github.com/oschwartz10612/poppler-windows/releases
- Extract to `OCR master/poppler/` directory

### 8. Test Your Setup

```bash
python test_api.py
```

Expected output:
```
API Key loaded: sk-or-v1-xxxxxxxxx...
Testing DeepSeek V3.2 model on OpenRouter...
Status Code: 200
Success! Response: 1
```

## Running Your First Analysis

### 1. Prepare Your Documents

Place PDF files in the `OCR input output/` directory:
```bash
mkdir -p "OCR input output"
cp /path/to/your/documents/*.pdf "OCR input output/"
```

### 2. Run OCR Processing

```bash
python ocr_vision.py
```

This will create `*_ocr.txt` files for each PDF.

### 3. Configure Your Research Criteria

Edit `prompt.py` and replace the placeholder text with your actual research criteria:

```python
USER_PROMPT_TEMPLATE = """Analyze if this document matches the following research criteria:

CRITERIA TO EVALUATE:
- Discusses renewable energy technologies
- Focuses on solar or wind power
- Published after 2015
- Contains technical specifications or performance data

Instructions:
- Read the document carefully
- Check if it meets ALL or MOST of the specified criteria
- Be reasonably strict but not overly rigid

Respond ONLY with:
1 = Document is relevant (matches the criteria)
0 = Document is not relevant (does not match the criteria)

Document text:
{document_text}"""
```

### 4. Move OCR Files to Analysis Directory

```bash
mkdir -p db
mv "OCR input output"/*_ocr.txt db/
```

### 5. Run Relevance Analysis

```bash
python document_filter.py
```

### 6. Review Results

```bash
cat relevance_results.csv
```

Or open in a spreadsheet application.

## Workflow Summary

```
1. PDF Documents → OCR input output/
2. Run: python ocr_vision.py
3. Move: *_ocr.txt files → db/
4. Edit: prompt.py (define criteria)
5. Run: python document_filter.py
6. Review: relevance_results.csv
```

## Common Issues and Solutions

### Issue: "GOOGLE_APPLICATION_CREDENTIALS not set"

**Solution:** Check that:
- `.env` file exists in the `OCR master/` directory
- The path to your credentials JSON file is correct
- No typos in the environment variable name

### Issue: "Error converting PDF"

**Solution:**
- Ensure Poppler is installed correctly
- On macOS/Linux, verify with: `which pdftoimage`
- On Windows, check the `poppler/` directory exists

### Issue: "OPENROUTER_API_KEY not set"

**Solution:**
- Verify the API key is in the `.env` file
- Ensure no extra spaces or quotes around the key
- Check the key is still valid at OpenRouter

### Issue: High API Costs

**Solution:**
- Start with a small batch of documents (2-3)
- Reduce character limit in `document_filter.py`:
  ```python
  doc_text = document_text[:1500]  # Reduced from 3000
  ```
- Monitor usage in Google Cloud Console and OpenRouter dashboard

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize prompts for your specific research needs
- Set up batch processing for large document collections
- Check [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute

## Getting Help

If you encounter issues:
1. Check the Troubleshooting section in README.md
2. Review API documentation for provider-specific errors
3. Create an issue on GitHub with details about your problem

## Cost Estimation

**For 100 documents (average 10 pages each):**
- Google Cloud Vision: ~$1.50 (1000 pages at $1.50/1000)
- OpenRouter (DeepSeek): ~$0.50-1.00 (depends on text length)
- **Total: ~$2-2.50**

Always start with a small test batch to verify costs for your specific use case.


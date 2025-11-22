# Research Paper Filter - LLM-Powered Document Relevance Analyzer

An intelligent document filtering system designed to help researchers quickly identify relevant papers and filter out irrelevant documents. The system uses OCR to extract text from PDF documents, then leverages large language models to analyze and determine relevance based on user-defined criteria.

## Overview

This tool automates the tedious process of manually reviewing academic papers and documents to determine their relevance to specific research questions. By combining optical character recognition with large language model analysis, it processes PDF documents at scale and filters them based on customizable research criteria.

## Key Features

- **Automated OCR Processing**: Extracts text from PDF documents using Google Cloud Vision API
- **LLM-Based Relevance Analysis**: Utilizes advanced language models (DeepSeek V3.2) via OpenRouter to evaluate document relevance
- **Customizable Filtering Criteria**: Easily configure filtering parameters to match your specific research needs
- **Batch Processing**: Process multiple documents efficiently with detailed progress tracking
- **Structured Output**: Generate CSV reports with relevance scores for easy review and further analysis
- **Error Handling**: Robust retry mechanisms and comprehensive error logging

## System Architecture

The system operates in two main stages:

1. **OCR Stage** (`ocr_vision.py`): Converts PDF documents to machine-readable text
2. **Filtering Stage** (`document_filter.py`): Analyzes extracted text using LLM to determine relevance

## Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account with Vision API enabled
- OpenRouter API account for LLM access
- Poppler utilities for PDF processing

## Installation

### 1. Clone the Repository

```bash
git clone git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git
cd "Research-Paper-Filter---Document-Relevance-Analyzer"
```

### 2. Install Python Dependencies

Navigate to the OCR master directory and install requirements:

```bash
cd "OCR master"
pip install -r requirements.txt
```

### 3. Set Up Poppler

Download and extract Poppler to the `poppler/` directory within the project:

```
OCR master/
  poppler/
    poppler-24.02.0/
      Library/
        bin/
```

Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases (for Windows) or use package managers for macOS/Linux:

- **macOS**: `brew install poppler`
- **Linux**: `apt-get install poppler-utils`

### 4. Configure Environment Variables

Create a `.env` file in the `OCR master/` directory with the following variables:

```env
# Google Cloud Vision API Credentials
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/google-cloud-credentials.json

# OpenRouter API Key
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

#### Obtaining API Keys:

**Google Cloud Vision API:**
1. Create a project in Google Cloud Console
2. Enable the Cloud Vision API
3. Create a service account and download the JSON credentials file
4. Set the path to this file in `GOOGLE_APPLICATION_CREDENTIALS`

**OpenRouter API:**
1. Sign up at https://openrouter.ai/
2. Generate an API key from your dashboard
3. Add the key to `OPENROUTER_API_KEY`

## Usage

### Step 1: OCR Processing

Place your PDF documents in the `OCR master/OCR input output/` directory, then run:

```bash
cd "OCR master"
python ocr_vision.py
```

This will:
- Process all PDF files in the input directory
- Extract text from each page using Google Cloud Vision API
- Save the extracted text to `*_ocr.txt` files in the same directory

### Step 2: Customize Filtering Criteria

Edit the `OCR master/prompt.py` file to define your research criteria:

```python
USER_PROMPT_TEMPLATE = """Analyze if this document matches the following criteria:

Criteria:
- Discusses climate change policy in developing nations
- Focuses on the period between 2000-2020
- Mentions carbon emissions or renewable energy

Respond ONLY with:
1 = Yes, matches the criteria
0 = No, does not match the criteria

Document:
{document_text}"""
```

### Step 3: Run Relevance Analysis

Move the OCR text files to the `OCR master/db/` directory, then run:

```bash
cd "OCR master"
python document_filter.py
```

This will:
- Analyze each OCR text file against your criteria
- Generate relevance scores (1 for relevant, 0 for not relevant)
- Save results to `relevance_results.csv`

### Step 4: Review Results

Open `relevance_results.csv` to see the analysis results:

```csv
filename,relevant
document1_ocr.txt,1
document2_ocr.txt,0
document3_ocr.txt,1
```

## Project Structure

```
Data extractor/                    # Root directory
├── README.md                      # This file
├── .gitignore                     # Git ignore rules
├── .gitattributes                 # Git attributes
├── relevance_results.csv          # Top-level results (optional)
└── OCR master/                    # Main application directory
    ├── ocr_vision.py              # OCR processing script
    ├── document_filter.py         # LLM-based relevance filtering
    ├── prompt.py                  # Customizable filtering prompts
    ├── test_api.py                # API connection testing utility
    ├── requirements.txt           # Python dependencies
    ├── .env                       # Environment variables (not in repo)
    ├── .gitignore                 # Additional ignore rules
    ├── LICENSE                    # MIT License
    ├── CONTRIBUTING.md            # Contribution guidelines
    ├── QUICKSTART.md              # Quick start guide
    ├── WORKFLOW.md                # Workflow documentation
    ├── SECURITY_CHECKLIST.md      # Security best practices
    ├── db/                        # OCR text files for analysis
    │   ├── *_ocr.txt              # Extracted text files
    │   └── *.pdf                  # Original PDF documents
    ├── OCR input output/          # PDF input and OCR output
    ├── poppler/                   # Poppler binaries (not in repo)
    └── relevance_results.csv      # Analysis results output
```

## Customization Guide

### Defining Your Research Criteria

The `prompt.py` file contains two templates that you should customize:

1. **USER_PROMPT_TEMPLATE**: Main prompt for initial analysis
2. **USER_PROMPT_RETRY_TEMPLATE**: Stricter prompt for retry attempts

#### Example Criteria Types:

**Topic-Based:**
```
- Discusses machine learning applications in healthcare
- Mentions neural networks or deep learning
```

**Methodology-Based:**
```
- Uses quantitative research methods
- Includes statistical analysis or experimental design
```

**Geographic:**
```
- Focuses on European Union countries
- Covers trans-Atlantic relations
```

**Temporal:**
```
- Covers events from 1990-2000
- Discusses historical developments in the Cold War era
```

**Theory-Based:**
```
- Applies social constructivist theory
- Uses rational choice or game theory frameworks
```

### Adjusting LLM Parameters

In `document_filter.py`, you can modify the LLM configuration:

```python
"model": "deepseek/deepseek-v3.2-exp",  # Change model
"temperature": 0.0,                      # Adjust randomness (0-1)
"max_tokens": 10                         # Response length limit
```

### Text Length Limitation

By default, only the first 3000 characters are analyzed to manage API costs:

```python
doc_text = document_text[:3000]  # Adjust as needed
```

## Error Handling

The system includes multiple error handling mechanisms:

- **Invalid LLM Responses**: Automatic retry with stricter prompts
- **API Failures**: Comprehensive error logging with status codes
- **OCR Errors**: Continues processing remaining files after errors
- **Missing Files**: Clear error messages for configuration issues

## Cost Considerations

- **Google Cloud Vision API**: Charged per 1000 images processed
- **OpenRouter API**: Charged per token (input + output)

To minimize costs:
- Reduce the character limit in `document_filter.py`
- Process documents in smaller batches
- Use lower-cost models if acceptable for your use case

## Testing

Test your API connections before processing large batches:

```bash
cd "OCR master"
python test_api.py
```

This verifies:
- Environment variables are loaded correctly
- API keys are valid
- Network connectivity to API endpoints

## Troubleshooting

### Common Issues

**Issue**: `GOOGLE_APPLICATION_CREDENTIALS not set`
- **Solution**: Ensure `.env` file exists and contains the correct path to your Google Cloud credentials JSON file

**Issue**: `Error converting PDF`
- **Solution**: Verify Poppler is installed correctly and the path in `ocr_vision.py` matches your installation

**Issue**: `OPENROUTER_API_KEY not set`
- **Solution**: Check that your `.env` file includes a valid OpenRouter API key

**Issue**: LLM returns invalid responses
- **Solution**: The system automatically retries with stricter prompts. If issues persist, adjust temperature or try a different model

**Issue**: High API costs
- **Solution**: Reduce character limit, process fewer documents, or switch to a more cost-effective model

## Performance

- **OCR Speed**: Approximately 5-10 seconds per page (depends on API response time)
- **LLM Analysis**: 1-3 seconds per document (depends on model and text length)
- **Batch Processing**: Handles hundreds of documents with progress tracking

## Contributing

Contributions are welcome. Please ensure:
- Code follows existing style conventions
- New features include appropriate error handling
- Documentation is updated for any API changes

## License

This project is provided as-is for research purposes. Ensure compliance with Google Cloud Platform and OpenRouter terms of service.

## API Documentation

- **Google Cloud Vision API**: https://cloud.google.com/vision/docs
- **OpenRouter API**: https://openrouter.ai/docs
- **DeepSeek Models**: https://platform.deepseek.com/

## Acknowledgments

This tool leverages:
- Google Cloud Vision API for OCR capabilities
- OpenRouter for LLM API access
- DeepSeek V3.2 for document analysis
- Poppler for PDF rendering

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review API documentation for provider-specific issues
3. Verify environment configuration with `test_api.py`

## Version History

- **v1.0.0**: Initial release with OCR and LLM-based filtering capabilities

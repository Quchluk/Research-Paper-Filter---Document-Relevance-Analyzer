# System Workflow Diagram

## Document Processing Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     RESEARCH PAPER FILTER                       │
│              LLM-Powered Document Relevance Analyzer            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                         INPUT STAGE                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   PDF Documents  │
                    │  (Research Papers)│
                    └──────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      STAGE 1: OCR PROCESSING                    │
│                      (ocr_vision.py)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Convert PDF to    │
                   │ Images (Poppler)  │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Google Cloud      │
                   │ Vision API OCR    │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Extract Text      │
                   │ from Each Page    │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Save as           │
                   │ *_ocr.txt files   │
                   └───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   STAGE 2: RELEVANCE ANALYSIS                   │
│                   (document_filter.py)                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Load OCR Text     │
                   │ Files from db/    │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Load Custom       │
                   │ Criteria from     │
                   │ prompt.py         │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Send to LLM       │
                   │ (DeepSeek V3.2)   │
                   │ via OpenRouter    │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Receive Relevance │
                   │ Score: 1 or 0     │
                   └───────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
          Invalid Response?             │
                    │                   │
                    ▼                   ▼
         ┌──────────────────┐    ┌─────────────┐
         │ Retry with       │    │ Valid Score │
         │ Strict Prompt    │    └─────────────┘
         └──────────────────┘           │
                    │                   │
                    └─────────┬─────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        OUTPUT STAGE                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Compile Results   │
                   │ to CSV File       │
                   └───────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ relevance_results │
                   │     .csv          │
                   │                   │
                   │ filename,relevant │
                   │ doc1_ocr.txt,1    │
                   │ doc2_ocr.txt,0    │
                   └───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCHER REVIEW                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌───────────────────┐
                   │ Filter Relevant   │
                   │ Documents for     │
                   │ Further Analysis  │
                   └───────────────────┘
```

## Component Interaction

```
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│                  │      │                  │      │                  │
│  ocr_vision.py   │──────│  document_       │──────│    prompt.py     │
│                  │      │  filter.py       │      │                  │
│  - PDF to text   │      │  - Text analysis │      │  - Filtering     │
│  - Google Vision │      │  - OpenRouter    │      │    criteria      │
│                  │      │  - Result output │      │  - LLM prompts   │
└──────────────────┘      └──────────────────┘      └──────────────────┘
         │                         │                         │
         │                         │                         │
         ▼                         ▼                         ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  Google Cloud    │      │   OpenRouter     │      │  User-Defined    │
│  Vision API      │      │   (DeepSeek)     │      │  Research        │
│                  │      │                  │      │  Criteria        │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```

## Configuration Flow

```
┌──────────────────┐
│   .env file      │
│  - API Keys      │
│  - Credentials   │
└────────┬─────────┘
         │
         ├──────────────────┬──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ GOOGLE_         │ │ OPENROUTER_     │ │  python-dotenv  │
│ APPLICATION_    │ │ API_KEY         │ │  loads vars     │
│ CREDENTIALS     │ │                 │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
         │                  │
         │                  │
         ▼                  ▼
┌──────────────────────────────────────┐
│   Application Components             │
│   - ocr_vision.py uses Vision API    │
│   - document_filter.py uses OpenRouter│
└──────────────────────────────────────┘
```

## Data Flow

```
PDF Files  →  OCR Processing  →  Text Files  →  LLM Analysis  →  CSV Results
   │              │                  │               │               │
   │              │                  │               │               │
   ▼              ▼                  ▼               ▼               ▼
Research      Google Cloud       *_ocr.txt       DeepSeek       relevance_
Papers        Vision API         Format          V3.2 via       results.csv
(Input)       (Conversion)       (Interim)       OpenRouter     (Output)
                                                  (Analysis)
```

## Error Handling Flow

```
┌─────────────────┐
│ Process Document│
└────────┬────────┘
         │
         ▼
    ┌────────┐
    │ Success?│
    └───┬────┘
        │
    ┌───┴────┐
    │        │
    Yes      No
    │        │
    │        ▼
    │   ┌──────────────┐
    │   │ Retry Once   │
    │   └──────┬───────┘
    │          │
    │      ┌───┴────┐
    │      │        │
    │      Yes      No
    │      │        │
    ▼      ▼        ▼
┌─────────────────────────┐
│  Log Result             │
│  - Success: Score       │
│  - Error: -1            │
│  Continue to Next File  │
└─────────────────────────┘
```

## Customization Points

```
┌──────────────────────────────────────────────────────────────┐
│              USER CUSTOMIZATION LOCATIONS                    │
└──────────────────────────────────────────────────────────────┘

1. prompt.py
   ├── USER_PROMPT_TEMPLATE
   │   └── Define your research criteria here
   │
   └── USER_PROMPT_RETRY_TEMPLATE
       └── Same criteria, stricter format

2. document_filter.py
   ├── Model selection (line ~41)
   │   └── Change LLM model if needed
   │
   ├── Temperature (line ~42)
   │   └── Adjust randomness (0.0-1.0)
   │
   └── Character limit (line ~18)
       └── Adjust text length analyzed

3. .env
   ├── GOOGLE_APPLICATION_CREDENTIALS
   │   └── Path to your Google Cloud credentials
   │
   └── OPENROUTER_API_KEY
       └── Your OpenRouter API key
```

## Directory Structure

```
OCR master/
│
├── Input/Processing
│   ├── OCR input output/     ← Place PDF files here
│   └── db/                   ← Place OCR text files here
│
├── Core Scripts
│   ├── ocr_vision.py         ← Stage 1: OCR
│   ├── document_filter.py    ← Stage 2: Analysis
│   ├── prompt.py             ← Customization
│   └── test_api.py           ← Testing
│
├── Configuration
│   ├── .env                  ← Your credentials (not in git)
│   ├── .env.example          ← Template
│   └── requirements.txt      ← Dependencies
│
├── Documentation
│   ├── README.md             ← Main docs
│   ├── QUICKSTART.md         ← Setup guide
│   ├── CONTRIBUTING.md       ← Contribution guide
│   └── SECURITY_CHECKLIST.md ← Security guide
│
└── Output
    └── relevance_results.csv ← Analysis results
```

## Typical Workflow Timeline

```
Step 1: Setup (One-time)          [30-60 minutes]
├── Install Python dependencies
├── Set up Google Cloud Vision
├── Set up OpenRouter account
└── Configure environment variables

Step 2: Customize Criteria        [10-15 minutes]
└── Edit prompt.py with your research needs

Step 3: OCR Processing            [~10 seconds per page]
├── Place PDFs in input directory
└── Run ocr_vision.py

Step 4: Relevance Analysis        [~2 seconds per document]
├── Move OCR files to db/
└── Run document_filter.py

Step 5: Review Results            [Variable]
└── Open relevance_results.csv

Total for 100 documents (~10 pages each):
- OCR: ~15-20 minutes
- Analysis: ~3-5 minutes
- Total: ~20-25 minutes
```


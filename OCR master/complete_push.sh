#!/bin/zsh

# Complete Git Push Script
# This script will initialize git, commit, and push to GitHub

echo "Starting Git push process..."
echo ""

# Change to the project directory
cd "/Users/Tosha/Desktop/Projects/Launcher/Data extractor/OCR master"

echo "Current directory: $(pwd)"
echo ""

# Initialize git
echo "1. Initializing Git repository..."
git init
echo ""

# Add all files
echo "2. Adding files to Git..."
git add .
echo ""

# Show what will be committed
echo "3. Files to be committed:"
git status --short
echo ""

# Create commit
echo "4. Creating commit..."
git commit -m "Initial commit: LLM-powered document filtering system

- Add OCR processing with Google Cloud Vision API
- Add LLM-based relevance analysis with DeepSeek
- Include comprehensive documentation
- Add configuration templates and examples
- Include MIT license and contribution guidelines"
echo ""

# Add remote (if not already added)
echo "5. Adding GitHub remote..."
git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git 2>/dev/null || echo "Remote already exists"
echo ""

# Verify remote
echo "6. Verifying remote..."
git remote -v
echo ""

# Set branch to main
echo "7. Setting branch to main..."
git branch -M main
echo ""

# Push to GitHub
echo "8. Pushing to GitHub..."
git push -u origin main
echo ""

echo "=========================================="
echo "✓ Successfully pushed to GitHub!"
echo "=========================================="
echo ""
echo "Your repository is now available at:"
echo "https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer"
echo ""
echo "What's been uploaded:"
echo "  ✓ Complete documentation (README, QUICKSTART, CONTRIBUTING, etc.)"
echo "  ✓ Source code (ocr_vision.py, document_filter.py, prompt.py)"
echo "  ✓ Configuration files (.gitignore, .env.example, requirements.txt)"
echo "  ✓ License and security documentation"
echo ""
echo "What's been excluded (sensitive/private):"
echo "  ✓ .env file (your API credentials)"
echo "  ✓ *.json files (Google Cloud credentials)"
echo "  ✓ *.pdf files (your research documents)"
echo "  ✓ *_ocr.txt files (processed text)"
echo "  ✓ relevance_results.csv (analysis results)"
echo ""
echo "Next steps:"
echo "  1. Visit your repository on GitHub"
echo "  2. Add topics/tags for better discoverability"
echo "  3. Enable Issues if you want bug reports"
echo "  4. Share with the research community!"
echo ""


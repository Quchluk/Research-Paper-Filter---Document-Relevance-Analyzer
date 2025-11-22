#!/bin/zsh

# Script to push the correct root folder to GitHub
# Root folder: /Users/Tosha/Desktop/Projects/Launcher/Data extractor

set -e  # Exit on error

echo "=========================================="
echo "Pushing Data extractor to GitHub"
echo "=========================================="
echo ""

# Navigate to the root folder
cd "/Users/Tosha/Desktop/Projects/Launcher/Data extractor"

echo "✓ Current directory: $(pwd)"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git repository already initialized"
fi
echo ""

# Check for sensitive files
echo "Checking for sensitive files..."
if git ls-files --error-unmatch .env >/dev/null 2>&1 || \
   git ls-files --error-unmatch "*.json" | grep -q "credentials\|booming-modem" 2>/dev/null; then
    echo "⚠️  WARNING: Sensitive files detected in git tracking!"
    echo "Please review and remove them before pushing."
    exit 1
fi
echo "✓ No sensitive files detected in tracking"
echo ""

# Check current remote
echo "Checking git remote..."
if git remote get-url origin >/dev/null 2>&1; then
    CURRENT_REMOTE=$(git remote get-url origin)
    echo "Current remote: $CURRENT_REMOTE"

    # If remote is different, update it
    if [ "$CURRENT_REMOTE" != "git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git" ]; then
        echo "Updating remote to correct repository..."
        git remote set-url origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git
        echo "✓ Remote updated"
    fi
else
    echo "Adding remote..."
    git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git
    echo "✓ Remote added"
fi
echo ""

# Stage all files
echo "Staging files..."
git add .
echo "✓ Files staged"
echo ""

# Show what will be committed
echo "Files to be committed:"
git status --short
echo ""

# Create commit
echo "Creating commit..."
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "No changes to commit"
else
    git commit -m "Initial commit: LLM-powered document filtering system

- Add OCR processing with Google Cloud Vision API
- Add LLM-based relevance analysis with DeepSeek
- Include comprehensive documentation
- Add configuration templates and examples
- Include MIT license and contribution guidelines
- Root folder structure with OCR master subdirectory"
    echo "✓ Commit created"
fi
echo ""

# Set branch to main
echo "Setting branch to main..."
git branch -M main
echo "✓ Branch set to main"
echo ""

# Push to GitHub (force push to replace wrong folder)
echo "Pushing to GitHub..."
echo "⚠️  Using --force to replace previously pushed wrong folder"
git push -u origin main --force

echo ""
echo "=========================================="
echo "✓ Successfully pushed to GitHub!"
echo "=========================================="
echo ""
echo "Repository: https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer"
echo ""


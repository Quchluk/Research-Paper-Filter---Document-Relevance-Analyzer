# Instructions to Push Root Folder to GitHub

## Current Situation
You previously pushed the wrong folder (OCR master subdirectory) to GitHub. 
Now we need to push the correct root folder: `/Users/Tosha/Desktop/Projects/Launcher/Data extractor`

## Repository Details
- **Repository**: git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git
- **Root folder**: `/Users/Tosha/Desktop/Projects/Launcher/Data extractor`

## Step-by-Step Instructions

### Step 1: Navigate to the Root Folder
```bash
cd "/Users/Tosha/Desktop/Projects/Launcher/Data extractor"
```

### Step 2: Verify You're in the Right Place
```bash
pwd
# Should show: /Users/Tosha/Desktop/Projects/Launcher/Data extractor

ls
# Should show: README.md, OCR master/, .gitignore, etc.
```

### Step 3: Initialize Git (if not already done)
```bash
git init
```

### Step 4: Configure Remote
```bash
# Remove existing remote if it exists
git remote remove origin 2>/dev/null

# Add the correct remote
git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git

# Verify remote
git remote -v
```

### Step 5: Stage All Files
```bash
git add .
```

### Step 6: Check What Will Be Committed
```bash
git status
```

**IMPORTANT**: Make sure sensitive files are NOT staged:
- No `.env` files
- No `booming-modem-*.json` credentials files
- These should be in `.gitignore` already

### Step 7: Create Initial Commit
```bash
git commit -m "Initial commit: LLM-powered document filtering system

- Add OCR processing with Google Cloud Vision API
- Add LLM-based relevance analysis with DeepSeek
- Include comprehensive documentation
- Add configuration templates and examples
- Include MIT license and contribution guidelines
- Root folder structure with OCR master subdirectory"
```

### Step 8: Set Branch to Main
```bash
git branch -M main
```

### Step 9: Push to GitHub (Force Push)
This will replace the incorrect folder structure that was pushed earlier:

```bash
git push -u origin main --force
```

### Step 10: Verify the Push
Visit the repository on GitHub:
https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer

You should see:
- README.md at the root
- OCR master/ as a subdirectory
- All other root-level files

## Troubleshooting

### If you get SSH permission errors:
1. Set up SSH keys for GitHub (https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
2. Or use HTTPS instead:
   ```bash
   git remote set-url origin https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git
   git push -u origin main --force
   ```

### If you get "nothing to commit" error:
This means the repository is already in sync. Verify on GitHub that the structure is correct.

### If files are too large:
Check `.gitignore` to make sure large files (PDFs, OCR outputs) are excluded.

## Alternative: One-Line Command
If you want to execute all steps at once:

```bash
cd "/Users/Tosha/Desktop/Projects/Launcher/Data extractor" && \
git init && \
git remote remove origin 2>/dev/null; \
git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git && \
git add . && \
git commit -m "Initial commit: Push root folder with correct structure" && \
git branch -M main && \
git push -u origin main --force
```

## After Successful Push
1. Visit https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer
2. Verify the folder structure is correct
3. Delete the helper scripts if you want:
   - push_to_github.py
   - push_to_github.sh
   - simple_push.sh
   - PUSH_INSTRUCTIONS.md (this file)


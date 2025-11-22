# Pre-Push Security Checklist

Before pushing your code to GitHub, ensure all sensitive information is excluded.

## Critical Items to Verify

### 1. Environment Variables
- [ ] `.env` file is NOT tracked by git
- [ ] `.env.example` exists and contains no real credentials
- [ ] Run: `git status` and confirm `.env` is not listed

### 2. API Credentials
- [ ] No Google Cloud JSON credentials in repository
- [ ] No hardcoded API keys in any Python files
- [ ] All credentials are loaded from environment variables

### 3. Document Files
- [ ] No PDF files in git tracking
- [ ] No OCR text output files tracked
- [ ] No personal or sensitive documents included

### 4. Results and Logs
- [ ] `relevance_results.csv` is not tracked
- [ ] No log files included
- [ ] No temporary files tracked

### 5. Binary Files
- [ ] Poppler binaries are not tracked (users will install separately)
- [ ] No large binary files included

## Verification Commands

Run these commands before pushing:

```bash
# Check what will be committed
git status

# Check for accidentally tracked sensitive files
git ls-files | grep -E '\\.env$|\\.json$|\\.pdf$'

# If any sensitive files are found, remove them
git rm --cached <filename>

# Verify .gitignore is working
git check-ignore -v .env
git check-ignore -v "*.json"
git check-ignore -v "*.pdf"
```

## If You Accidentally Commit Secrets

If you accidentally commit API keys or credentials:

1. **Immediately revoke the exposed credentials**
   - Google Cloud: Delete and recreate service account key
   - OpenRouter: Revoke and generate new API key

2. **Remove from git history**
   ```bash
   # For recent commit
   git reset --soft HEAD~1
   
   # For older commits (use with caution)
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch path/to/sensitive/file" \
     --prune-empty --tag-name-filter cat -- --all
   ```

3. **Force push (if already pushed)**
   ```bash
   git push --force
   ```

## Final Pre-Push Check

```bash
# Review all files that will be pushed
git diff --name-only origin/main

# Review actual content being pushed
git diff origin/main
```

## Safe to Commit

These files SHOULD be in your repository:
- ✓ `README.md`
- ✓ `LICENSE`
- ✓ `CONTRIBUTING.md`
- ✓ `QUICKSTART.md`
- ✓ `.gitignore`
- ✓ `.env.example`
- ✓ `requirements.txt`
- ✓ `*.py` files (verify no hardcoded secrets inside)

## After Pushing

1. Visit your GitHub repository
2. Browse through files online
3. Confirm no sensitive data is visible
4. Check the commit history for accidental inclusions

## Emergency Contact

If you discover exposed secrets after pushing:
1. Revoke all exposed credentials immediately
2. Follow GitHub's guide: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
3. Consider making the repository private temporarily

---

**Remember:** Once pushed to GitHub, assume any exposed credentials are compromised, even if you delete them immediately. Prevention is key.


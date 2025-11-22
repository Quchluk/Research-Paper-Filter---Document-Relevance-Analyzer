#!/usr/bin/env python3
import subprocess
import os
import sys

# Change to the root directory
root_dir = "/Users/Tosha/Desktop/Projects/Launcher/Data extractor"
os.chdir(root_dir)

print("="*50)
print("Pushing Data extractor root folder to GitHub")
print("="*50)
print(f"\nCurrent directory: {os.getcwd()}\n")

def run_command(cmd, description):
    """Run a shell command and print output"""
    print(f"→ {description}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=root_dir
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

        if result.returncode != 0:
            print(f"✗ Command failed with return code {result.returncode}")
            # Don't exit for certain expected errors
            if "already exists" not in result.stderr and "nothing to commit" not in result.stderr:
                return False
        else:
            print("✓ Success\n")
        return True
    except Exception as e:
        print(f"✗ Error: {e}\n")
        return False

# Step 1: Check if .git exists
if not os.path.exists(".git"):
    print("Initializing git repository...")
    run_command("git init", "Initializing git")
else:
    print("✓ Git repository already exists\n")

# Step 2: Check/add remote
print("Checking remote configuration...")
result = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
if result.returncode != 0:
    # Remote doesn't exist, add it
    run_command(
        "git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git",
        "Adding GitHub remote"
    )
else:
    current_remote = result.stdout.strip()
    target_remote = "git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git"
    print(f"Current remote: {current_remote}")
    if current_remote != target_remote:
        run_command(
            f"git remote set-url origin {target_remote}",
            "Updating remote URL"
        )
    else:
        print("✓ Remote is already correctly configured\n")

# Step 3: Stage files
run_command("git add .", "Staging all files")

# Step 4: Show status
run_command("git status --short", "Showing staged files")

# Step 5: Check if there are changes to commit
result = subprocess.run("git diff-index --quiet HEAD --", shell=True, capture_output=True)
if result.returncode != 0:
    # There are changes
    commit_msg = """Initial commit: LLM-powered document filtering system

- Add OCR processing with Google Cloud Vision API
- Add LLM-based relevance analysis with DeepSeek
- Include comprehensive documentation
- Add configuration templates and examples
- Include MIT license and contribution guidelines
- Root folder structure with OCR master subdirectory"""

    run_command(
        f'git commit -m "{commit_msg}"',
        "Creating commit"
    )
else:
    print("No changes to commit\n")

# Step 6: Set branch to main
run_command("git branch -M main", "Setting branch to main")

# Step 7: Push to GitHub
print("⚠️  Pushing to GitHub with --force to replace wrong folder structure")
success = run_command("git push -u origin main --force", "Pushing to GitHub")

if success:
    print("\n" + "="*50)
    print("✓ Successfully pushed to GitHub!")
    print("="*50)
    print("\nRepository URL:")
    print("https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer")
    print("\nVerify the push by visiting the repository URL above.")
else:
    print("\n" + "="*50)
    print("✗ Push may have failed")
    print("="*50)
    print("\nIf you see SSH permission errors, you may need to:")
    print("1. Set up SSH keys for GitHub")
    print("2. Or use HTTPS instead:")
    print("   git remote set-url origin https://github.com/Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git")
    print("   git push -u origin main --force")


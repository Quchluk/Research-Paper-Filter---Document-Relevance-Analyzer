#!/bin/zsh

cd "/Users/Tosha/Desktop/Projects/Launcher/Data extractor"

echo "Starting push process..." > push_log.txt
echo "Current directory: $(pwd)" >> push_log.txt

git init >> push_log.txt 2>&1
git remote remove origin >> push_log.txt 2>&1
git remote add origin git@github.com:Quchluk/Research-Paper-Filter---Document-Relevance-Analyzer.git >> push_log.txt 2>&1
git add . >> push_log.txt 2>&1
git commit -m "Initial commit: Push root folder with OCR master subdirectory" >> push_log.txt 2>&1
git branch -M main >> push_log.txt 2>&1
git push -u origin main --force >> push_log.txt 2>&1

echo "Push complete!" >> push_log.txt
echo "Check push_log.txt for details"

cat push_log.txt


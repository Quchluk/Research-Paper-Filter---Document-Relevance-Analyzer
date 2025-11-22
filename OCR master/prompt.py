"""
Document Relevance Analysis - Prompt Configuration

INSTRUCTIONS FOR CUSTOMIZATION:
--------------------------------
This file controls how documents are filtered based on your research criteria.
You MUST customize the prompts below to match your specific research needs.

STEP 1: Define Your Filtering Criteria
---------------------------------------
Think about what makes a document relevant to your research:

- TOPIC: What subject matter must the document cover?
  Example: "nuclear proliferation", "climate policy", "artificial intelligence"

- METHODOLOGY: What research methods are you interested in?
  Example: "quantitative analysis", "case studies", "ethnographic research"

- GEOGRAPHY: What regions or countries should be covered?
  Example: "Middle East", "European Union", "Southeast Asia"

- TIME PERIOD: What historical period should the document address?
  Example: "Cold War era (1947-1991)", "post-2000", "1990s"

- KEY TERMS: What specific concepts, technologies, or theories?
  Example: "machine learning", "game theory", "renewable energy"

- DOCUMENT TYPE: What kind of documents are you looking for?
  Example: "policy briefs", "technical reports", "diplomatic cables"

STEP 2: Edit the Templates Below
---------------------------------
Replace the placeholder text in both USER_PROMPT_TEMPLATE and
USER_PROMPT_RETRY_TEMPLATE with your specific criteria.

Both templates should contain the SAME criteria - the retry template
is just more strict in its format requirements.
"""

SYSTEM_PROMPT = "You are a document relevance analyzer. Respond only with 1 (relevant) or 0 (not relevant)."

SYSTEM_PROMPT_RETRY = "You are a document analyzer. You MUST respond with ONLY the number 1 or 0. Nothing else. 1 means relevant, 0 means not relevant."

# CUSTOMIZE THIS: Replace the placeholder criteria with your research requirements
USER_PROMPT_TEMPLATE = """Analyze if this document matches the following research criteria:

CRITERIA TO EVALUATE:
[REPLACE THIS SECTION WITH YOUR SPECIFIC CRITERIA]

Instructions:
- Read the document carefully
- Check if it meets ALL or MOST of the specified criteria
- Be reasonably strict but not overly rigid

Respond ONLY with:
1 = Document is relevant (matches the criteria)
0 = Document is not relevant (does not match the criteria)

Document text:
{document_text}"""

# CUSTOMIZE THIS: Must contain the SAME criteria as above
USER_PROMPT_RETRY_TEMPLATE = """Determine if this document matches the specified research criteria.

CRITERIA TO EVALUATE:
[REPLACE THIS SECTION WITH YOUR SPECIFIC CRITERIA - SAME AS ABOVE]

Your response must be EXACTLY one character:
- 1 if the document matches the criteria
- 0 if it does not match the criteria

No explanation. No additional text. Only '1' or '0'.

Document text:
{document_text}"""

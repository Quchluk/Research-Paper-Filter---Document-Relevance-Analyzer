# Contributing to Research Paper Filter

Thank you for considering contributing to this project. This document provides guidelines for contributing to the Research Paper Filter system.

## How to Contribute

### Reporting Issues

If you encounter bugs or have suggestions for improvements:

1. Check the existing issues to avoid duplicates
2. Create a new issue with a clear title and description
3. Include relevant details:
   - Python version
   - Operating system
   - Error messages and stack traces
   - Steps to reproduce the issue

### Code Contributions

1. **Fork the Repository**
   ```bash
   git clone <your-fork-url>
   cd "Data extractor/OCR master"
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Your Changes**
   - Ensure all existing functionality still works
   - Test edge cases and error conditions
   - Verify API integrations function correctly

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Explain the motivation for the changes

## Code Style Guidelines

### Python Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use docstrings for functions and classes

Example:
```python
def process_document(file_path):
    """
    Process a document and extract relevant information.
    
    Args:
        file_path (str): Path to the document file
        
    Returns:
        dict: Extracted information from the document
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    # Implementation here
    pass
```

### Error Handling

- Always include try-except blocks for external API calls
- Provide informative error messages
- Log errors appropriately
- Allow the system to continue processing other files after errors

Example:
```python
try:
    result = api_call()
except APIError as e:
    print(f"API Error: {e}")
    return None
except Exception as e:
    print(f"Unexpected error: {e}")
    raise
```

### Documentation

- Update README.md if adding new features
- Add docstrings to all functions
- Comment complex logic
- Update requirements.txt if adding dependencies

## Areas for Contribution

### High Priority

- Support for additional OCR engines (Tesseract, AWS Textract)
- Alternative LLM providers (OpenAI, Anthropic, local models)
- Batch processing optimization
- Progress bars and better logging
- Unit tests and integration tests

### Medium Priority

- Web interface for configuration and monitoring
- Support for more document formats (DOCX, HTML)
- Parallel processing for faster throughput
- Database integration for result storage
- Resume functionality for interrupted processing

### Low Priority

- GUI application
- Docker containerization
- Cloud deployment scripts
- Advanced analytics and visualization
- Multi-language document support

## Testing Guidelines

### Manual Testing

1. Test with various PDF types:
   - Scanned documents
   - Digital PDFs
   - Multi-page documents
   - Documents with images and tables

2. Test error conditions:
   - Invalid API keys
   - Network failures
   - Corrupted PDFs
   - Missing dependencies

3. Test edge cases:
   - Empty documents
   - Very large documents
   - Non-English text
   - Special characters

### Automated Testing

When adding tests:
- Place test files in a `tests/` directory
- Use pytest framework
- Name test files with `test_` prefix
- Aim for >80% code coverage

## Pull Request Process

1. Ensure your code follows the style guidelines
2. Update documentation to reflect your changes
3. Add or update tests as appropriate
4. Ensure all tests pass
5. Update the Version History in README.md
6. Request review from maintainers

## Code Review Process

Reviewers will check for:
- Code quality and style compliance
- Proper error handling
- Documentation completeness
- Test coverage
- Performance implications
- Security considerations

## Questions or Need Help?

- Review existing documentation
- Check closed issues for similar questions
- Create a new issue with the "question" label

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be acknowledged in the project documentation. Thank you for helping improve the Research Paper Filter system.


# Testing Guide

Welcome! This guide explains how testing works in the tldr-pages project in simple, easy-to-understand language. Whether you're contributing for the first time or maintaining the project, this guide has you covered.

## Table of Contents

- [Why We Test](#why-we-test)
- [Quick Start - Run Tests Locally](#quick-start---run-tests-locally)
- [What Gets Tested?](#what-gets-tested)
- [Understanding Test Results](#understanding-test-results)
- [Automated Testing (CI/CD)](#automated-testing-cicd)
- [Test Tools Explained](#test-tools-explained)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
- [Writing Test-Friendly Pages](#writing-test-friendly-pages)

## Why We Test?

Tests help us ensure that:

- All pages follow the same format and style
- Markdown syntax is correct
- Links work properly
- Translations match their English versions
- Code follows best practices
- Changes don't break existing pages

Think of tests as your friendly assistant that catches mistakes before they reach the main repository!

## Quick Start - Run Tests Locally

### Prerequisites

Before running tests, make sure you have these installed:

1. **Node.js** (version 18 or higher)

   ```bash
   node --version
   ```

2. **Python** (version 3.12 or higher)

   ```bash
   python3 --version
   ```

3. **Git** (to clone the repository)
   ```bash
   git --version
   ```

### Step-by-Step: Run All Tests

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/tldr-pages/tldr.git
   cd tldr
   ```

2. **Install dependencies**:

   ```bash
   # Install Node.js dependencies
   npm install

   # Install Python dependencies
   pip3 install -r requirements.txt
   ```

3. **Run the tests**:

   ```bash
   npm test
   ```

   That's it! The tests will run automatically.

### Step-by-Step: Run Specific Tests

You can also run individual test tools:

- **Check Markdown formatting**:

  ```bash
  npm run lint-markdown
  ```

- **Check tldr page format**:

  ```bash
  npm run lint-tldr-pages
  ```

- **Check Python code formatting** (if you modified Python scripts):

  ```bash
  black scripts --check
  ```

- **Check Python code style** (if you modified Python scripts):
  ```bash
  flake8 scripts
  ```

---

## What Gets Tested?

Here's a breakdown of what our tests check:

### 1. **Markdown Linting** (`markdownlint`)

Checks that your Markdown files are properly formatted:

- Correct heading levels
- Proper list formatting
- No trailing spaces
- Consistent line breaks

**Example error**: "MD041: First line in file should be a top-level heading"

### 2. **tldr Page Linting** (`tldr-lint`)

Ensures pages follow the [tldr style guide](contributing-guides/style-guide.md):

- Correct page structure (title, description, examples)
- Proper placeholder format (`{{example}}`)
- Maximum 8 examples per page
- Correct use of backticks and hyphens
- "More information" links are present

**Example error**: "TLDR001: Too many examples in page (found 10, max 8)"

### 3. **Python Code Quality** (`black`, `flake8`, `pytest`)

If you modify any Python scripts:

- **black**: Ensures consistent code formatting
- **flake8**: Checks for coding style issues
- **pytest**: Runs unit tests on Python scripts

### 4. **Shell Script Quality** (`shellcheck`)

Checks that shell scripts are well-written and safe

### 5. **Pull Request Checks** (`check-pr.sh`)

Special checks that run on pull requests:

- **Duplicate detection**: Ensures pages aren't duplicated across platforms
- **English page existence**: Verifies translations have English originals
- **Outdated translations**: Flags translations that don't match English pages
- **Common vs platform-specific**: Checks if pages should be in `common/` instead

## Understanding Test Results

### All Tests Pass

```
 markdownlint passed
 tldr-lint passed
 black passed
 flake8 passed
Test ran successfully!
```

**What to do**: Great job! Your changes are ready to submit.

---

### Tests Failed

Don't worry! Test failures are normal and help you improve your contribution.

#### Example 1: Markdown Formatting Error

```
pages/common/example.md:5 MD022/blanks-around-headings
Headings should be surrounded by blank lines
```

**What it means**: Line 5 needs blank lines before and after the heading.

**How to fix**:

```diff
  > More information: <https://example.com>.
+
  # example
+
  > Short description.
```

---

#### Example 2: tldr-lint Error

```
pages/common/tar.md: TLDR001: Number of command examples is not between 1 and 8
```

**What it means**: Your page has more than 8 examples (or less than 1).

**How to fix**: Remove extra examples or add more if you have too few.

---

#### Example 3: Python Formatting Error

```
scripts/test.py: E501 line too long (88 > 79 characters)
```

**What it means**: A line in your Python code is too long.

**How to fix**: Break the line into multiple lines or run:

```bash
black scripts/test.py
```

---

### Pull Request Warnings

These don't fail the build but are suggestions:

```
- pages/linux/tar.md already exists under 'common', consider removing this page
```

**What it means**: The page might belong in `common/` instead of `linux/`.

**What to do**: Review the suggestion and decide if it applies.

---

## Automated Testing (CI/CD)

Every time you create a pull request, **GitHub Actions** automatically runs tests. Here's what happens:

### The Testing Pipeline

1. **Setup Environment**

   - Install Node.js and Python
   - Install all dependencies

2. **Run Tests**

   - Markdown linting
   - tldr-lint checks
   - Python code quality checks
   - Shell script checks

3. **Run PR-Specific Checks**

   - Check for duplicates
   - Check for missing English pages
   - Check for outdated translations

4. **Build Artifacts** (main branch only)

   - Generate ZIP archives
   - Generate PDF documentation

5. **Deploy** (main branch only)
   - Deploy to the website

### Where to See Results

On your pull request page, you'll see:

- **Green checkmark**: All tests passed!
- **Red X**: Tests failed (click "Details" to see why)
- **Yellow dot**: Tests are still running

### tldr-bot Comments

If tests fail, **tldr-bot** will automatically comment on your PR with details about what went wrong. Look for comments like:

```
 tldr-bot here!

I found some issues with your changes:

pages/common/example.md:
- TLDR001: Too many examples (found 9, expected max 8)
```

## Test Tools Explained

Here's what each testing tool does:

| Tool             | Purpose              | What It Checks                             |
| ---------------- | -------------------- | ------------------------------------------ |
| **markdownlint** | Markdown formatting  | Proper Markdown syntax, consistent style   |
| **tldr-lint**    | tldr page format     | Style guide compliance, placeholder format |
| **black**        | Python formatting    | Consistent Python code style               |
| **flake8**       | Python code quality  | Python best practices, error detection     |
| **pytest**       | Python unit tests    | Functionality of Python scripts            |
| **shellcheck**   | Shell script quality | Shell script best practices                |
| **check-pr.sh**  | PR validation        | Duplicates, missing pages, translations    |

## Troubleshooting Common Issues

### Problem: `markdownlint: command not found`

**Solution**: Install Node.js dependencies:

```bash
npm install
```

### Problem: `tldr-lint: command not found`

**Solution**: Install Node.js dependencies:

```bash
npm install
```

### Problem: `black: command not found`

**Solution**: Install Python dependencies:

```bash
pip3 install -r requirements.txt
```

### Problem: Tests pass locally but fail on GitHub

**Possible reasons**:

1. You didn't commit all your changes
2. Your local dependencies are outdated
3. You're testing different files

**Solution**:

```bash
# Make sure everything is committed
git status

# Update dependencies
npm install
pip3 install -r requirements.txt

# Run tests again
npm test
```

### Problem: "All done!" message but tests still fail

This can happen with `black` when the version doesn't match.

**Solution**: Install the exact version specified:

```bash
pip3 install -r requirements.txt
```

## Writing Test-Friendly Pages

Follow these tips to ensure your pages pass all tests:

### DO:

```markdown
# command-name

> Short, clear description.
> More information: <https://example.com>.

- Example description:

`command --option {{argument}}`

- Another example:

`command {{path/to/file}}`
```

### DON'T:

```markdown
# command-name

> Missing blank line above

> Missing space after >
> More information: example.com (missing angle brackets)

- Example with no blank line after:
  `command --option argument` (missing placeholder)

- Example with no blank line before description
  `command --option`
```

### Checklist Before Submitting

- Page has a proper title (`# command-name`)
- Description is 1-2 lines with a "More information" link
- Between 1 and 8 examples
- Each example has a description (starting with `-`)
- Commands use proper placeholders (`{{like_this}}`)
- All examples are in code blocks (backticks)
- Blank lines separate sections
- File is saved in the correct platform directory
  These checklist needs to be followed properly.

## Additional Resources

- **Style Guide**: [contributing-guides/style-guide.md](contributing-guides/style-guide.md)
- **Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Test Scripts**: [scripts/README.md](scripts/README.md)
- **GitHub Actions**: [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Need Help?

If you're stuck or have questions:

1. **Check the error message carefully** - it usually tells you exactly what's wrong
2. **Look at existing pages** - see how others solved similar problems
3. **Ask in the Matrix chat**: [#tldr-pages:matrix.org](https://matrix.to/#/#tldr-pages:matrix.org)
4. **Open an issue**: Describe what you're trying to do and what error you're getting

Remember: Everyone makes mistakes! Tests are here to help, not to judge. Keep trying, and you'll get it right!

**Happy Contributing!**

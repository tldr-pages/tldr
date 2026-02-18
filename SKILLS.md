# TLDR Pages - AI Assistant Guide

This guide helps AI assistants understand and work with the tldr-pages repository effectively.

## Quick Decision Workflow

```text
User asks about command X
        │
        ▼
┌─────────────────────┐
│ Does page exist?    │
│ find pages* -name   │
│ "X.md"              │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
   YES          NO
    │           │
    ▼           ▼
┌─────────┐  ┌──────────────────────┐
│ Edit    │  │ Which platform?      │
│ existing│  └──────────┬───────────┘
└─────────┘             │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
          2+ same   1 platform  Windows
          syntax    only        
              │         │         │
              ▼         ▼         ▼
          common/   <platform>/  windows/
          
              │
              ▼
    ┌─────────────────────┐
    │ Create page with    │
    │ 5-8 examples        │
    │ (help/version last) │
    └─────────────────────┘
```

## Project Overview

**tldr-pages** is a collection of community-maintained, simplified help pages for command-line tools - a simpler complement to traditional man pages.

- **License**: CC BY 4.0 (pages), MIT (scripts)
- **Website**: https://tldr.sh/
- **Repository**: https://github.com/tldr-pages/tldr
- **Languages Supported**: 30+ translations

## Repository Structure

```text
tldr/
tldr/
├── pages/                    # English (default) pages
│   ├── common/              # Commands on 2+ platforms
│   ├── linux/               # Linux-only
│   ├── osx/                 # macOS-only
│   ├── windows/             # Windows-only
│   ├── android/             # Android-only
│   └── ...                  # Other platforms
├── pages.<locale>/          # Translations
│   ├── pages.fr/            # French
│   ├── pages.es/            # Spanish
│   └── ...                  # 30+ languages
├── scripts/                 # Python utility scripts
├── contributing-guides/     # Documentation
└── .github/                 # CI/CD workflows
```

## Core Concepts

### Page

A single Markdown file documenting one command.

### Platform

Operating system directories: `common`, `linux`, `osx`, `windows`, `android`, `freebsd`, `openbsd`, `netbsd`, `sunos`, `cisco-ios`, `dos`.

### Placeholder

User-provided values in double brackets: `{{path/to/file}}`, `{{filename}}`, `{{host}}`.

### Alias Page

Redirects users to another command (e.g., `vi` → `vim`).

### Subcommand Page

Separate pages for subcommands like `git commit` → `git-commit.md`.

## Page Format Specification

Every tldr page MUST follow this template (max 8 examples):

```markdown
# command-name

> Short, snappy description.
> Preferably one line; two are acceptable if necessary.
> More information: <https://url-to-upstream.tld>.

- Example description:

`command --option`

- Example description:

`command --option1 --option2 {{arg_value}}`
```

### Format Rules

1. **Title**: Must match filename exactly (case-insensitive in content, lowercase in filename)
2. **Description Lines**: Start with `>`, 1-2 lines preferred
3. **More Information Link**: Required, wrapped in `< >`
4. **Examples**: 5 preferred, 8 maximum
5. **Description**: Start with `- `, use imperative mood
6. **Command**: Wrapped in backticks on separate line after description
7. **Blank Lines**: Required between examples

## Style Guidelines

### Writing Style

- **Imperative mood**: "List all files" NOT "Lists all files"
- **Concise**: Focus on practical examples
- **No formatting**: No *italics*, **bold**, or other markdown styling
- **Avoid general concepts**: Don't explain UNIX basics

### Placeholder Conventions

| Pattern | Usage |
| ------- | ----- |
| `{{path/to/file}}` | File paths |
| `{{path/to/directory}}` | Directory paths |
| `{{filename}}` | Just filename |
| `{{file1 file2 ...}}` | Multiple arguments |
| `{{option1\|option2}}` | Alternatives |
| `{{[-v\|--verbose]}}` | Option choice (client decides) |
| `{{1..5}}` | Numeric range |
| `{{*.ext}}` | Wildcard pattern |
| `{{path/to/file_or_directory}}` | Either file or directory |

### Option Syntax

- Prefer long options: `--help` over `-h`
- Use option placeholders: `{{[-o|--output]}}`
- Group flags: `{{[-it|--interactive --tty]}}`
- Space before args: `--option arg` NOT `--option=arg`
- Short option mnemonic hints: `[c]reate`, `[v]erbose`

### Keypress Syntax

- Single: `<a>`, `<Enter>`, `<Space>`
- Special: `<Ctrl>`, `<Alt>`, `<Shift>` (PascalCase)
- Combinations: `<Ctrl c>`, `<Alt F4>`
- Sequence: `<Esc><u>`, `<Ctrl k><Ctrl s>`

### Help and Version Commands

We generally put the help and version commands as the **last two** examples of the page (in this order) to highlight more practical commands at the beginning. They can be replaced to accommodate other useful examples if required.

For consistency, we prefer generic wording `Display help` and `Display version` for these commands.

It is suggested to document the help and version examples if the command follows unconventional flags in platforms like Windows.

### Heading Order

```markdown
> Short description.
> Further clarification if needed.
> Some subcommands such as `commit`, `push` have their own usage documentation.
> See also: `command1`, `command2`.
> More information: <https://example.com>.
```

## Platform-Specific Rules

### Windows

- **Filename**: lowercase (e.g., `invoke-webrequest.md`)
- **Title**: as-is (`# Invoke-WebRequest`)
- **Command**: as-is (`Invoke-WebRequest`)
- **Paths**: backslashes `{{path\to\file}}`
- **Environment vars**: `%VARIABLE%` (cmd), `$Env:VARIABLE` (PowerShell)
- **PowerShell compatibility**: Must work on 5.1 and latest

### Common Directory

Use when command works on 2+ platforms with same syntax.

### Platform-Specific Directory

Use when command works on only ONE platform.

## Alias Pages

Template for command aliases:

```markdown
# alias-name

> This command is an alias of `original-command`.
> More information: <https://example.com>.

- View documentation for the original command:

`tldr original-command`
```

## Creating Pages

### New Page Workflow

1. **Determine platform**:
   - 2+ platforms → `pages/common/`
   - 1 platform → `pages/<platform>/`

2. **Create file**: `pages/<platform>/<command>.md`

3. **Write content** following format specification

4. **Test locally**:

   ```bash
   npm install -g tldr-lint
   tldr-lint path/to/page.md
   ```

5. **Commit**:

   ```bash
   git add pages/<platform>/<command>.md
   git commit -m "<command>: add page"
   ```

### Editing Pages

Commit format: `<command>: <description>`

Examples:

- `ls: fix typo`
- `git-push: add --force example`
- `tar: update description`

### Translations

1. Ensure English page exists first
2. Create: `pages.<locale>/<platform>/<command>.md`
3. Translate following language-specific rules
4. Commit: `<command>: add <language> translation`

## Language-Specific Rules

### Chinese (zh, zh_TW)

- Space around English/numbers: `docker 容器` not `docker容器`
- Space between numbers and units (except °C, %): `50 MB` not `50MB`
- Full-width punctuation

### Indonesian (id)

- No `ber-`/`me-` prefixes: "Unduh" not "Mengunduh"
- Use recommended technical terms

### French (fr)

- Third person singular present: "Extrait" not "Extraire"
- Space before punctuation: ` informations : ` not ` informations: `

### Portuguese (pt_BR, pt_PT)

- Third person singular present: "Lista" not "Listar"

### Spanish (es)

- Third person singular indicative: "Crea" not "Crear"
- Use `identificador` not `id` in placeholders

## Testing & Validation

### Linting

```bash
# Install linter
npm install -g tldr-lint

# Lint single page
tldr-lint pages/common/tar.md

# Lint all pages
tldr-lint ./pages

# Via npm
npm run lint-tldr-pages
```

### Pre-commit Hooks

Tests run automatically on commit via Husky.
Skip with: `git commit --no-verify`

### Available Scripts

In `scripts/` directory:

| Script | Purpose |
| ------ | ------- |
| `set-alias-page.py` | Create/update alias pages |
| `set-more-info-link.py` | Update documentation links |
| `set-page-title.py` | Update page titles |
| `set-see-also.py` | Update "See also" references |
| `update-command.py` | Update command examples |
| `wrong-filename.py` | Find naming issues |

**Common flags for all scripts**:

- `-p, --page`: Target page (format: `platform/command`)
- `-l, --language`: Target locale
- `-s, --stage`: Stage changes with git
- `-n, --dry-run`: Preview without applying
- `-S, --sync`: Sync translations

Example:

```bash
python scripts/set-alias-page.py -p common/vi -n  # Dry run
python scripts/set-alias-page.py -p common/vi -s  # Apply & stage
```

## Common Tasks for AI Assistants

### Adding a New Command Page

When asked to create a page for a command:

1. Check if page already exists: `find pages* -name "<command>.md"`
2. Determine correct platform directory
3. Research command options (man page, --help, official docs)
4. Write 5-8 practical examples following format
5. Include help and version examples (usually last 2)
6. Test with tldr-lint
7. Provide git commands to commit

### Translating Pages

When translating:

1. Always start from English page
2. Maintain same example structure
3. Follow language-specific grammar rules
4. Keep placeholders in English
5. Don't translate `example.com`
6. Verify with native speaker if possible

### Reviewing PRs

#### Manual Review Checklist

Check for:

- [ ] Correct format (title, description, examples)
- [ ] Imperative mood in descriptions
- [ ] Proper placeholder syntax
- [ ] Appropriate platform directory
- [ ] Max 8 examples
- [ ] "More information" link present
- [ ] No bold/italics/styling
- [ ] Follows language-specific rules (for translations)

#### AI-Assisted Review

PR reviewers can use AI assistants with this guide to automate validation:

**1. Automated Format Checking** — review format compliance:

```text
Review this PR for format compliance:
- Verify page follows template structure
- Check for proper heading order
- Validate placeholder syntax ({{}} not {} or ())
- Ensure blank lines between examples
- Confirm "More information" link is present
```

**2. Style Validation** — check for style issues:

```text
Check these pages for style issues:
- Verify imperative mood in descriptions ("List" not "Lists")
- Check for bold/italics/styling violations
- Validate placeholder naming (snake_case, descriptive)
- Ensure no general UNIX concepts explained
```

**3. Platform Directory Verification** — verify correct directory:

```text
Verify platform directory is correct:
- Check if command works on multiple platforms → common/
- Verify single-platform commands are in correct directory
- Check for existing pages in other platforms
```

**4. Translation Review** — review translation PRs:

```text
Review this translation PR:
- Verify based on current English page (not outdated version)
- Check language-specific grammar rules
- Ensure placeholders remain in English
- Verify example count matches English page
```

See [Common Mistakes](#common-mistakes) for detailed examples of issues to flag.

## Useful Resources

- **Full Style Guide**: `contributing-guides/style-guide.md`
- **Translation Templates**: `contributing-guides/translation-templates/`
- **Client Spec**: `CLIENT-SPECIFICATION.md`
- **Contributing**: `CONTRIBUTING.md`
- **Translation Dashboard**: https://lukwebsforge.github.io/tldri18n/
- **Linter**: https://github.com/tldr-pages/tldr-lint

## Quick Reference Templates

### Basic Page Template

```markdown
# command

> Brief description.
> More information: <https://example.com>.

- Description of example:

`command {{arg}}`

- Another example:

`command {{[-f|--flag]}}`

- Display help:

`command --help`

- Display version:

`command --version`
```

### Alias Page Template

```markdown
# alias

> This command is an alias of `original`.
> More information: <https://example.com>.

- View documentation for the original command:

`tldr original`
```

### Subcommand Reference Template

```markdown
# command

> Brief description.
> Some subcommands such as `sub1`, `sub2` have their own usage documentation.
> More information: <https://example.com>.

- Common usage:

`command {{arg}}`

- View documentation for subcommand:

`tldr command-sub1`
```

### Disambiguation Template

```markdown
# command

> `command` can refer to multiple commands with the same name.

- View documentation for context 1:

`tldr command.1`

- View documentation for context 2:

`tldr command.2`
```

## Environment Setup

```bash
# Clone repository
git clone https://github.com/tldr-pages/tldr.git
cd tldr

# Install Node dependencies
npm install

# Install tldr-lint globally
npm install -g tldr-lint

# Optional: Install tldr client for preview
pipx install tldr
# or
brew install tlrc
```

## Common "More Information" URLs

- https://manned.org/[command] - General man pages
- https://www.gnu.org/software/[command]/manual/ - GNU tools
- https://learn.microsoft.com/powershell/module/... - PowerShell
- https://learn.microsoft.com/windows-server/... - Windows commands
- https://keith.github.io/xcode-man-pages/ - macOS built-ins
- https://docs.python.org/3/library/... - Python modules
- https://docs.npmjs.com/cli/... - npm commands
- https://docs.docker.com/engine/reference/commandline/... - Docker
- https://kubernetes.io/docs/reference/generated/kubectl/... - kubectl
- https://git-scm.com/docs/... - Git commands

## Examples of Good Pages

Simple: `pages/common/pwd.md`
With placeholders: `pages/common/tar.md`
With subcommands: `pages/common/git.md`
With aliases: `pages/common/vi.md`
Windows-specific: `pages/windows/Invoke-WebRequest.md`

## Common Mistakes

### Format Errors

**Missing blank line between examples:**

```markdown
- List files:
`ls -la`
- List all files:
`ls -la --all`
```

**Correct:**

```markdown
- List files:

`ls -la`

- List all files:

`ls -la --all`
```

### Style Errors

**Non-imperative mood:**

```markdown
- Lists all files in the directory:

`ls -la`
```

**Correct:**

```markdown
- List all files in the directory:

`ls -la`
```

**Using bold/italics:**

```markdown
- **Delete** a file permanently:

`rm -rf {{file}}`
```

**Correct:**

```markdown
- Delete a file permanently:

`rm -rf {{file}}`
```

### Placeholder Errors

**Wrong placeholder syntax:**

```markdown
`cp {source} {destination}`
`cp (source) (destination)`
`cp [source] [destination]`
```

**Correct:**

```markdown
`cp {{path/to/source}} {{path/to/destination}}`
```

**Nested placeholders:**

```markdown
`mkdir {{path/to/{{directory}}}}`
```

**Correct:**

```markdown
`mkdir {{path/to/directory}}`
```

**Missing "More information" link:**

```markdown
# command

> Brief description.

- Example:

`command --help`
```

**Correct:**

```markdown
# command

> Brief description.
> More information: <https://example.com>.

- Example:

`command --help`
```

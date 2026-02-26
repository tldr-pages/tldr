# TLDR Pages - AI Assistant Guide

This guide helps AI assistants contribute to tldr-pages effectively. For detailed rules, see `contributing-guides/style-guide.md`.

## Quick Decision Workflow

```text
User asks about command X
        │
        ▼
Does page exist? (find pages* -name "X.md")
        │
   ┌────┴────┐
  YES        NO
   │          │
   ▼          ▼
Edit      Which platform?
          │
     ┌────┼────┐
  2+ same  1 platform  Windows
     │       │         │
     ▼       ▼         ▼
  common/  linux/    windows/
                    osx/ etc.
```

## Project Overview

**tldr-pages** - Community-maintained simplified help pages for command-line tools.

- **License**: CC BY 4.0 (pages), MIT (scripts)
- **Website**: https://tldr.sh/
- **Languages**: 30+ translations in `pages.<locale>/`

## Repository Structure

```
pages/           # English pages
  ├── common/    # 2+ platforms
  ├── linux/     # Linux-only
  ├── osx/       # macOS-only
  ├── windows/   # Windows-only
  └── ...        # android, freebsd, openbsd, netbsd, sunos, cisco-ios, dos
pages.<locale>/  # Translations (fr, es, zh, etc.)
scripts/         # Python utilities
```

## Page Format

```markdown
# command-name

> Short, snappy description (1-2 lines max).
> More information: <https://url-to-upstream.tld>.

- Description of example:

`command --option {{path/to/file}}`

- Another example:

`command {{[-f|--flag]}} {{arg}}`

- Display help:

`command {{[-h|--help]}}`

- Display version:

`command {{[-V|--version]}}`
```

### Format Rules

1. **Title**: Match filename exactly (lowercase in filename, case-insensitive in content)
2. **Description**: Start with `>`, 1-2 lines preferred
3. **More Information**: Required, wrapped in `< >`
4. **Examples**: 5 preferred, 8 maximum
5. **Descriptions**: Start with `- `, use **imperative mood** ("List" not "Lists")
6. **Commands**: Wrapped in backticks, separate line after description
7. **Blank Lines**: Required between examples
8. **Trailing Newline**: File must end with newline

## Style Guidelines

### Writing Style

- **Imperative mood**: "List all files" NOT "Lists all files"
- **Concise**: Focus on practical examples
- **No formatting**: No *italics*, **bold**, or other markdown styling
- **Avoid general concepts**: Don't explain UNIX basics

### Placeholder Conventions

| Pattern | Usage |
|---------|-------|
| `{{path/to/file}}` | File paths |
| `{{path/to/directory}}` | Directory paths |
| `{{filename}}` | Filename only |
| `{{file1 file2 ...}}` | Multiple arguments |
| `{{option1\|option2}}` | Alternatives |
| `{{[-v\|--verbose]}}` | Verbose output flag |
| `{{[-it\|--interactive --tty]}}` | Grouped flags |
| `{{1..5}}` | Numeric range |
| `{{*.ext}}` | Wildcard pattern |

### Option Syntax

- **When both forms exist**, use both: `{{[-h|--help]}}`
- **Verify flags exist**: Check `man <command>` or `<command> --help` before documenting
- Note: Version flag varies by command (`-V`, `--version`, or no short option) - check documentation
- Space before args: `--option arg` NOT `--option=arg`
- Short option hints: `[c]reate`, `[v]erbose`

### Keypress Syntax

- Single: `<a>`, `<Enter>`, `<Space>`
- Special: `<Ctrl>`, `<Alt>`, `<Shift>` (PascalCase)
- Combinations: `<Ctrl c>`, `<Alt F4>`
- Sequence: `<Esc><u>`, `<Ctrl k><Ctrl s>`

### More Information Link

- Verify URL is reachable and returns HTTP 200 (follows redirects):

```bash
# Check URL and status code
curl -sL -o /dev/null -w "%{http_code}" https://example.com/command
# Should return: 200
```

- Use official sources (man pages, docs, project sites)
- Preferred: https://manned.org/[command], https://www.gnu.org/software/[command]/manual/

### Help/Version Commands

Place as **last two** examples (in this order) to highlight practical commands first. Use wording: "Display help", "Display version".

## Platform-Specific Rules

### Windows

- **Filename**: lowercase (e.g., `invoke-webrequest.md`)
- **Title**: as-is (`# Invoke-WebRequest`)
- **Command**: as-is (`Invoke-WebRequest`)
- **Paths**: backslashes `{{path\to\file}}`
- **Environment vars**: `%VARIABLE%` (cmd), `$Env:VARIABLE` (PowerShell)
- **PowerShell compatibility**: Must work on 5.1 and latest

### Directory Selection

- **pages/common/**: Command works on 2+ platforms with same syntax
- **pages/<platform>/**: Command works on only ONE platform

## Alias Pages

Use `scripts/set-alias-page.py -p <platform>/<command> -l <locale>` for translations.

```markdown
# alias

> This command is an alias of `original`.
> More information: <https://example.com>.

- View documentation for the original command:

`tldr original`
```

## Subcommands

Commands with subcommands (like `git`) should mention them in the description:

```markdown
# command

> Brief description.
> Some subcommands such as `sub1`, `sub2`, etc. have their own usage documentation.
> More information: <https://example.com>.

- Common usage:

`command {{arg}}`

- View documentation for subcommand:

`tldr command-sub1`
```

**Note**: Each subcommand gets its own page: `git-commit.md`, `git-push.md`, etc.

## Creating Pages

1. Check existing: `find pages* -name "<command>.md"`
2. Determine platform → `pages/common/` (2+ platforms) or `pages/<platform>/`
3. Research: `man <command>`, `<command> --help`, official docs
4. Create file: `pages/<platform>/<command>.md`
5. Write content: 5-8 practical examples (help/version last)
6. Test: `tldr-lint path/to/page.md`
7. Commit: `git add pages/<platform>/<command>.md && git commit -m "<command>: add page"`

### Editing Pages

Commit format: `<command>: <description>` (e.g., `ls: fix typo`, `git-push: add --force example`)

### Translations

1. Ensure English page exists
2. **For alias pages**: Use `scripts/set-alias-page.py -p <platform>/<command> -l <locale>`
3. Create file: `pages.<locale>/<platform>/<command>.md`
4. Translate:
   - Maintain same example structure
   - Keep placeholders in English
   - Don't translate `example.com`
   - Follow language-specific rules below
5. Commit: `<command>: add <language> translation`

## Language-Specific Rules

### Chinese (zh)
- Space around English/numbers: `docker 容器`
- Full-width punctuation

### French (fr)
- Third person: "Extrait" not "Extraire"
- Space before punctuation: `informations :`

### Spanish (es)
- Third person: "Crea" not "Crear"
- Use `identificador` not `id`

### Portuguese (pt_BR, pt_PT)
- Third person: "Lista" not "Listar"

### Indonesian (id)
- No `ber-`/`me-` prefixes: "Unduh" not "Mengunduh"

## Testing & Validation

```bash
# Install linter
npm install -g tldr-lint

# Lint single page or all
tldr-lint pages/common/tar.md
tldr-lint ./pages

# Via npm
npm run lint-tldr-pages
```

### Available Scripts

In `scripts/` directory:

| Script | Purpose |
|--------|---------|
| `set-alias-page.py` | Create/update alias pages |
| `set-more-info-link.py` | Update documentation links |
| `set-page-title.py` | Update page titles |
| `set-see-also.py` | Update "See also" references |
| `update-command.py` | Update command examples |
| `wrong-filename.py` | Find naming issues |

**Flags**: `-p platform/command`, `-l locale`, `-s` (stage), `-n` (dry-run), `-S` (sync)

Example: `python scripts/set-alias-page.py -p common/vi -s`

## AI Review Checklist

When reviewing PRs, verify:

- [ ] Correct format (title, description, examples)
- [ ] Imperative mood in descriptions
- [ ] Proper placeholder syntax `{{}}`
- [ ] Both option forms used when available: `{{[-h|--help]}}`
- [ ] Appropriate platform directory
- [ ] Max 8 examples
- [ ] "More information" link present
- [ ] Help/version examples present with wording "Display help" and "Display version"
- [ ] No bold/italics/styling
- [ ] Blank lines between examples
- [ ] Language-specific rules (translations)

## Resources

- **Style Guide**: `contributing-guides/style-guide.md`
- **CONTRIBUTING.md**: General contribution guidelines
- **Translation Dashboard**: https://lukwebsforge.github.io/tldri18n/
- **Linter**: https://github.com/tldr-pages/tldr-lint

### Common URLs

- https://manned.org/[command] - General man pages
- https://www.gnu.org/software/[command]/manual/ - GNU tools
- https://learn.microsoft.com/powershell/module/... - PowerShell
- https://keith.github.io/xcode-man-pages/ - macOS
- https://git-scm.com/docs/[command] - Git

### Good Examples

- Simple: `pages/common/pwd.md`
- With placeholders: `pages/common/tar.md`
- With subcommands: `pages/common/git.md`
- With aliases: `pages/common/vi.md`
- Windows: `pages/windows/Invoke-WebRequest.md`

## Common Mistakes

**Wrong:**
```markdown
- Lists all files:
`ls -la`
- **Delete** a file:
`rm -rf {file}`
```

**Correct:**
```markdown
- List all files:

`ls -la`

- Delete a file:

`rm -rf {{path/to/file}}`
```

**Other issues:**
- Non-imperative mood: "Lists" instead of "List"
- Wrong placeholders: `{file}` or `[file]` instead of `{{file}}`
- Nested placeholders: `{{path/to/{{file}}}}`
- Missing "More information" link
- No blank lines between examples

## API Cost-Saving Tips

When using AI assistants to create tldr pages:

1. **Check for existing pages first**: Always run `find pages* -name "<command>.md"` before creating new pages to avoid redundant work

2. **Reuse patterns from similar commands**: Look at 2-3 existing pages (e.g., `pages/common/tar.md`, `pages/common/curl.md`) before generating new content instead of asking the AI to invent examples

3. **Provide command help output**: When asking for a new page, include the output of `<command> --help` or `man <command>` to reduce the AI's need to research

4. **Batch similar requests**: Group multiple related page creation requests together rather than making separate API calls

5. **Use the templates**: Reference the templates in this file directly instead of asking the AI to recall them from memory

6. **Verify with linter first**: Run `tldr-lint` before asking for human review to catch simple formatting errors

7. **Limit examples to 5-6**: Use the minimum viable number of examples (5 preferred) rather than maxing out at 8

**Remember**: These tips reduce API costs while maintaining output quality - the key is providing better context upfront so the AI generates correct content in fewer attempts.

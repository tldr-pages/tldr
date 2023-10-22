# Style guide

This page lists specific formatting instructions for `tldr` pages.

## Layout

The basic format of each page should match the following template and have at most 8 command examples:

```md
# command name

> Short, snappy command description.
> Preferably one line; two are acceptable if necessary.
> More information: <https://example.com/command_name/help/page>.

- Code description:

`command_name options`

- Code description:

`command_name options`

...
```

Example:

```md
# krita

> A sketching and painting program designed for digital artists.
> See also: `gimp`.
> More information: <https://docs.krita.org/en/reference_manual/linux_command_line.html>.

- Start Krita:

`krita`

- Open specific files:

`krita {{path/to/image1 path/to/image2 ...}}`

- Start without a splash screen:

`krita --nosplash`

- Start with a specific workspace:

`krita --workspace {{Animation}}`

- Start in fullscreen mode:

`krita --fullscreen`
```

> [!NOTE]
> The help page can be any documentation/project/tutorial page, not just a man page,
> but documentation pages are preferred.

There is a linter that enforces the format above.
It is run automatically on every pull request,
but you may install it to test your contributions locally before submitting them:

```sh
npm install --global tldr-lint
tldr-lint path/to/tldr_page.md
```

For other ways to use `tldr-lint`, such as linting an entire directory, check out (what else!)
[`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md). Alternatively, you can also use its alias `tldrl`.

Your client may be able to preview a page locally using the `--render` flag:

```sh
tldr --render path/to/tldr_page.md
```

### Aliases

If a command can be called with alternative names (like `vim` can be called by `vi`), alias pages can be created to point the user to the original command name.

```md
# command_name

> This command is an alias of `original-command-name`.
> More information: <https://example.com/original/command/help/page>.

- View documentation for the original command:

`tldr original_command_name`
```

Example:

```md
# vi

> This command is an alias of `vim`.

- View documentation for the original command:

`tldr vim`

```

- Pre-translated alias page templates can be found [here](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md).

## Option syntax

- Use GNU-style **long options** (like `--help` rather than `-h`) when they are cross-platform compatible (intended to work the same across multiple platforms).
- In other cases, use short options (like `-h`).
- Prefer using a space instead of the equals sign (`=`) to separate options from their arguments (i.e. use `--opt arg` instead of `--opt=arg`), unless the program does not support it.

## Placeholder syntax

User-provided values should use the `{{placeholder}}` syntax
in order to allow `tldr` clients to highlight them.

Keep the following guidelines in mind when choosing placeholders:

### Naming

- Use short but descriptive placeholders,
  such as `{{path/to/source_file}}` or `{{path/to/wallet.txt}}`.
- Use [`snake_case`](https://wikipedia.org/wiki/snake_case) for multi-word placeholders.
- Use a generic placeholder rather than an actual value where a generic placeholder is available (but there is an exception to this listed below). For example, use
  `iostat {{1..infinity}}` rather than `iostat {{2}}`.
  - If there are several consecutive placeholders of the same type
  which don't allow adding arbitrary text in them (ranges), then instead of generic placeholders use descriptive ones. For example prefer `input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{seconds}}`
  instead of `input swipe {{-infinity..infinity}} {{-infinity..infinity}} {{-infinity..infinity}} {{-infinity..infinity}} {{1..infinity}}`.

### Paths

- Use `{{filename}}` when just file name is expected.
- For any reference to paths of files or directories,
  use the format `{{path/to/<placeholder>}}`,
  except when the location is implicit.
- When the path cannot be relative,
  but has to start at the root of the filesystem,
  prefix it with a slash,
  such as `get {{/path/to/remote_file}}`.
- In case of a possible reference both to a file or a directory,
  use `{{path/to/file_or_directory}}`.

### Extensions

- If a particular extension is expected for the file, append it.
  For example, `unrar x {{path/to/compressed.rar}}`.
- In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
  For instance, in `find.md`'s example "Find files by extension" (`find {{path/to/root}} -name '{{*.ext}}'`)
  using `{{*.ext}}` explains the command without being unnecessarily specific;
  while in `wc -l {{path/to/file}}` using `{{path/to/file}}` (without extension) is sufficient.

### Grouping placeholders

- If a command can take 0 or more arguments of the same kind, use an ellipsis: `{{placeholder1 placeholder2 ...}}`.
  For instance, if multiple paths are expected `{{path/to/directory1 path/to/directory2 ...}}` can be used.
- If a command can take 0 or more arguments of different kinds, use an ellipsis: `{{placeholder1|placeholder2|...}}`.
  If there are more than 5 possible values use `|...` after the last item.
- It's impossible to restrict the minimum or (and) maximum placeholder count via `ellipsis`.

It's up to the program to decide how to handle duplicating values, provided syntax
tells no info about whether items are mutually exclusive or not.

### Special cases

- If a command performs irreversible changes to a file system or devices,
  write every example in a way that cannot be copy pasted thoughtlessly.
  For example, instead of `ddrescue --force --no-scrape /dev/sda /dev/sdb`
  write `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`
  and use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.

In general, placeholders should make it as intuitive as possible
to figure out how to use the command and fill it in with values.

Technical wording on description lines should use the `backtick` syntax.
Use backticks on the following:

- Paths, e.g. `package.json`, `/etc/package.json`.
- Extensions, e.g. `.dll`.
- Commands, e.g. `ls`.

## Descriptions

- Avoid using the page title in the description (e.g. use `A sketching and painting program designed for digital artists` instead of `Krita is a sketching and painting program designed for digital artists`) unless the program name differs from the executable name (e.g. `rg` and Ripgrep).
- Avoid mentioning that the program is used on the command-line (e.g. use `Ripgrep is a recursive line-oriented search tool` instead of `Ripgrep is a recursive line-oriented CLI search tool`).

### Imperative Mood

- **All descriptions must be concise and phrased in the imperative mood.**
- This also applies to all translations by default unless otherwise specified in the language-specific section below.
- For example, when writing documentation for `cd`, a tool to check out and work on a specific directory in the Terminal or Command Prompt, **do not** write a lengthy description such as:

```md
> `cd` is a system tool, available in Windows, macOS, and Linux, to check out a specific directory to get things done in the Command Prompt, Terminal, and PowerShell.
```

It should instead be simplified to make it easier for everyone to read:

```md
> Change the current working directory.
```

If you are afraid the commands may differ between platforms or operating systems (e.g. Windows vs macOS), most [tldr pages clients](https://github.com/tldr-pages/tldr/wiki/tldr-pages-clients) will choose the most suitable version of the command.

In this case, the information of the Windows version of `cd` (stored in `pages/windows/cd.md`) will be displayed by default to Windows users, and a generic/common version (stored in `pages/common/cd.md`) will be displayed for Linux, macOS, and other platforms.

When writing descriptions for command examples, **check for any grammatical errors**. `Go to the specified directory` is preferred instead of:

- `Going to the specified directory` (should not be in present participle form)
- `This command will go to the specified directory` (it is clear that this example works for *this* comment)
- `Let's go to the specified directory!`
- `Directory change` (use the active form instead of passive, if possible)

For instance, instead of `Listing all files:`, `List all files:` can be be used as the example's description below:

```md
- Listing all files:

 `ls`
```

## Serial Comma

- When declaring a list of 3 or more items,
use a [serial comma](https://en.wikipedia.org/wiki/Serial_comma),
also known as the Oxford comma,
since omitting it can create ambiguity.

> Delete the Git branches, tags and remotes.

The example above does not use a serial comma, so this could mean one of two things:

- Delete the Git branches named `tags` and `remotes`.
- Delete all of the following: Git branches, Git tags, and Git remotes.

This can be resolved by inserting a comma before the "and" or "or" in the final element in the list.

> Delete the Git branches, tags, and remotes.

## More information links

On the `More information` line, prefer linking to the author's provided documentation.

When not available, use <https://manned.org> as the default fallback.

## Language-Specific Rules

### Chinese-Specific Rules

When Chinese words, Latin words and Arabic numerals are written in the same sentence, more attention must be paid to copywriting.

The following guidelines are applied to Chinese (`zh`) and traditional Chinese (`zh_TW`) pages:

1. Place one space before/after English words and numbers.

 - For example, use `列出所有 docker 容器` rather than `列出所有docker容器`.
 - For example, use `宽度为 50 个字` rather than `宽度为50个字`.

2. Place one space between numbers and units **except** degrees and percentages.

 - For example, use `容量 50 MB` rather than `容量 50MB`.
 - For instances of degree and percentage, use `50°C` and `50%` rather than `50 °C` and `50 %`.

3. No additional spaces before/after full-width punctuations.

 - For example, use `开启 shell，进入交互模式` rather than `开启 shell ，进入交互模式`

4. Use full-width punctuations except for long Latin clauses.

 - For example, use `嗨，你好。` rather than `嗨, 你好.`

5. Use a half-width punctuation to end a sentence when the last character is half-width.

  - For example, use `将代码转化为 Python 3.` rather than `将代码转化为 Python 3。`

6. Use precise form for technical terms, and do not use unofficial Chinese abbreviations.

 - For example, use `Facebook` rather than `facebook`, `fb` or `脸书`.

In order to maintain readability and normalization, please comply with the 6 rules above as much as possible when translating pages into Chinese.

For more information and examples of Chinese-specific rules, check out [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en.md).

### French-Specific Rules

Example descriptions on pages in French must use the third person singular present indicative tense (présent de l'indicatif à la troisième personne du singulier).
For example, use `Extrait une archive` rather than `Extraire une archive` or `Extrais une archive`.

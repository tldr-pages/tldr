# Style guide

This page lists specific formatting instructions for `tldr` pages.

## Layout

The basic format of each page should match the following template:

```md
# <command-name>

> Short, snappy description.
> Preferably one line; two are acceptable if necessary.
> More information: <https://example.com>.

- Example description:

`<command-name> -opt1 -opt2 -arg1 {{arg_value}}`

- Example description:

`<command-name> -opt1 -opt2`
```

There actually is a linter/formatter that enforces the format above.
It is run automatically on every pull request,
but you may install it to test your contributions locally before submitting them:

```sh
npm install --global tldr-lint
tldr-lint {{page.md}}
```

For other ways to use `tldr-lint`, such as linting an entire directory, check out (what else!)
[`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md). Alternatively, you can also use its alias `tldrl`.

Your client may be able to preview a page locally using the `--render` flag:

```sh
tldr --render {{page.md}}
```

## Aliases

If some command is an alias for another then you can provide for it such Tl;Dr page:

```md
# command-name

> This command is an alias of `<original-command>`.
> More information: <original-command-help-page>.
- View documentation for the original command:

`tldr <original-command>`
```

## Token syntax

User-provided values should use the `{{token}}` syntax
in order to allow `tldr` clients to highlight them.

Keep the following guidelines in mind when choosing tokens:

### Naming

1. Use short but descriptive tokens, such as `{{source_file}}` or `{{wallet.txt}}`.
2. Use [`snake_case`](https://wikipedia.org/wiki/snake_case) for multi-word tokens.
3. Use an actual value rather than a generic placeholder where appropriate (such cases are described below).
  For example, use `iostat {{2}}` rather than `iostat {{interval_in_secs}}`.

### Paths

> :x: **Don't use** concreete values for paths unless documentation provides such ones explicitly.

#### File paths

> ✔️ **Use** `{{path/to/file.ext}}` generic placeholder for file path unless documentation provides any information about allowed values explicitly.

> ✔️ **Use** just one of most well known file extensions when more than 5 extensions are allowed by documentation or file name is not a placeholder. Otherwise list them via `|` character.

1. Use `{{filename}}` placeholder just when **no absolute/relative path is required**. In other case prefer `{{path/to/file}}`.
2. Use `{{filename.ext}}`/`{{path/to/file.ext}}` (where `.ext` is a file extension) placeholders just when **allowed extension is provided** (above rule applies here).
3. Replace `filename`/`file`/`ext` in placeholders described above with concreete values when **documentation provides cocreete file names/extensions**.
4. Replace `filename`/`file`/`ext` in placeholders described above with concreete values describing meaning of the argument when **argument used with short options/subcommands** to easily understand argument meaning.

> :scroll: **Example**: `unrar x {{path/to/compressed.rar}}` - `compressed.rar` is used instead of `path/to/file.ext` because it's hard to understand what is `compressed.rar`.

#### Directory paths

> :x: **Don't forget** add `/` for absolute paths.

> ✔️ **Use** `{{path/to/directory}}` generic placeholder for directory path unless documentation provides any information about allowed values explicitly.

1. Use `{{directory}}` placeholder just when **no absolute/relative path is required**. In other case prefer `{{path/to/directory}}`.
2. Replace `directory` in placeholders described above with concreete values when **documentation provides cocreete directory names** (above rule applies here).
3. Replace `directory` in placeholders described above with concreete values describing meaning of the argument when **argument used with short options/subcommands**  to easily understand argument meaning.

#### Mixing file names and directories

1. Use `|` as a delimiter **between** file/directory paths.
2. Place file path **before** directory one.
3. Use `{{file_or_directory}}` placeholder shorthand just when **no absolute/relative paths are required** and **no allowed extensions are provided**.
4. Use `{{path/to/file_or_directory}}` placeholder shorthand just when **absolute/relative paths are required** and **no allowed extensions are provided**.

> :scroll: **Examples**: `{{filename|directory}}`, `{{path/to/file.ext|directory}}`, `{{path/to/file.ext|path/to/directory}}`, `{{path/to/file_or_directory}}`.

### Flags

1. Use long flags when available for pages in `linux/` directory.
2. Always use short flags when available for pages in `osx/` and `windows/` directories.
3. Use short flags for frequently used options when available.

> :scroll: **Example**: `fish --command` (in `common/` directory) - `--command` is used instead of `-c` because it's hard to understand what is `-c`.

> :scroll: **Example**: `git commit -m` (in `common/` directory) - `-m` is used instead of `--message` because it's faster to type `-m` and it's frequently used.

### Special cases

1. If a command performs irreversible changes to a file system or devices,
  write every example in a way that they cannot be thoughtlessly copy-pasted.
  For example, instead of `ddrescue --force --no-scrape /dev/sda /dev/sdb`
  write `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`
  and use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.
2. If a command can take a variable number of arguments, use an ellipsis: `{{arg1 arg2 ...}}`
  If one of multiple options is possible, write it as `{{either|or}}`.

In general, tokens should make it as intuitive as possible
to figure out how to use the command and fill it in with values.

Technical wording on description lines should use the `backtick` syntax.
Use backticks on the following:

- Paths, ex. `package.json`, `/etc/package.json`.
- Extensions, ex. `.dll`.
- Commands, ex. `ls`.

## Imperative Mood

Example descriptions have to be phrased in imperative mood.
For example, use `List all files`, instead of `Listing all files` or `File listing`.
This also applies to all translations by default, unless this is not possible for some reason.

## Serial Comma

When declaring a list of 3 or more items,
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

When not available, use <https://manned.org/> as the default fallback.

## Tool oriented guides

- [How to write pages about shells?](https://github.com/tldr-pages/tldr/tree/main/contributing-guides/tool-oriented-guides/shells.md)

## Chinese-Specific Rules

When Chinese words, Latin words and Arabic numerals are written in the same sentence, it takes more attention to copywriting.

The following guidelines are applied to Chinese (zh) and traditional Chinese (zh_TW):

1. Place one space before/after English words and numbers.
   For example, use `列出所有 docker 容器` rather than `列出所有docker容器`.
   For example, use `宽度为 50 个字` rather than `宽度为50个字`.
2. Place one space between numbers and units **except** degrees and percentages.
   For example, use `容量 50 MB` rather than `容量 50MB`.
   For instances of degree and percentage, use `50°C` and `50%` rather than `50 °C` and `50 %`.
3. No additional spaces before/after full-width punctuations.
   For example, use `开启 shell，进入交互模式` rather than `开启 shell ，进入交互模式`
4. Use full-width punctuations except for long Latin clauses.
   For example, use `嗨，你好。` rather than `嗨, 你好.`
5. Use a half-width punctuation to end a sentence when the last character is half-width.
   For example, use `将代码转化为 Python 3.` rather than `将代码转化为 Python 3。`
6. Use precise form for technical terms, and do not use unofficial Chinese abbreviations.
   For example, use `Facebook` rather than `facebook`, `fb` or `脸书`.

In order to maintain readability and normalization, please comply the 6 rules above as much as possible when translating pages into Chinese.

For more information and examples of Chinese-specific rules, check out [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en-US.md).

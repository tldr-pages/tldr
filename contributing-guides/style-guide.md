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

> Krita is a sketching and painting program designed for digital artists.
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

> :bulb: The help page can be any documentation/project/tutorial page, not just a man page,
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

## Token syntax

User-provided values should use the `{{token}}` syntax
in order to allow `tldr` clients to highlight them.

Keep the following guidelines in mind when choosing tokens:

### Naming
- Use short but descriptive tokens,
  such as `{{source_file}}` or `{{wallet.txt}}`.
- Use [`snake_case`](https://wikipedia.org/wiki/snake_case) for multi-word tokens.
- Use an actual value rather than a generic placeholder where appropriate.
  For example, use `iostat {{2}}` rather than `iostat {{interval_in_secs}}`.

### Paths
- Use `{{filename}}` rather than `{{file_name}}`.
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
  For example, `unrar x {{compressed.rar}}`.
- In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
  For instance, in `find.md`'s example "Find files by extension" (`find {{root_path}} -name '{{*.ext}}'`)
  using `{{*.ext}}` explains the command without being unnecessarily specific;
  while in `wc -l {{file}}` using `{{file}}` (without extension) is sufficient.

### Special cases
- If a command performs irreversible changes to a file system or devices,
  write every example in a way that cannot be thoughtlessly copy-pasted.
  For example, instead of `ddrescue --force --no-scrape /dev/sda /dev/sdb`
  write `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`
  and use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.
- If a command can take a variable number of arguments, use an ellipsis: `{{arg1 arg2 ...}}`.
  If one of the multiple options is possible, write it as `{{either|or}}`.

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
This also applies to all translations by default, unless otherwise specified in the language-specific section below.  

## Serial Comma

When declaring a list of 3 or more items,
use a [serial comma](https://en.wikipedia.org/wiki/Serial_comma),
also known as the Oxford comma,
since omitting it can create ambiguity.

> Delete the Git branches, tags and remotes.

The example above does not use a serial comma, so this could mean one of two things:
* Delete the Git branches named `tags` and `remotes`.
* Delete all of the following: Git branches, Git tags, and Git remotes.

This can be resolved by inserting a comma before the "and" or "or" in the final element in the list.

> Delete the Git branches, tags, and remotes.

## More information links

On the `More information` line, prefer linking to the author's provided documentation.

When not available, use <https://manned.org> as the default fallback. 

## Language-Specific Rules

### Chinese-Specific Rules

When Chinese words, Latin words and Arabic numerals are written in the same sentence, more attention must be paid to copywriting.

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

In order to maintain readability and normalization, please comply with the 6 rules above as much as possible when translating pages into Chinese.

For more information and examples of Chinese-specific rules, check out [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en.md).

### French-Specific Rules

Example descriptions on pages in French must use the third person singular present indicative tense (présent de l'indicatif à la troisième personne du singulier).
For example, use `Extrait une archive` rather than `Extraire une archive` or `Extrais une archive`.

# Style guide

This page lists specific formatting instructions for `tldr` pages.

## Layout

The basic format of each page should match the following template:

```
# command-name

> Short, snappy description.
> Preferably one line; two are acceptable if necessary.
> More information: <https://example.com>.

- Example description:

`command -opt1 -opt2 -arg1 {{arg_value}}`

- Example description:

`command -opt1 -opt2`
```

There actually is a linter/formatter that enforces the format above.
It is run automatically on every pull request,
but you may install it to test your contributions locally before submitting them:

```
npm install tldr-lint
tldrl -f {{page.md}}
```

For other ways to use `tldrl`, such as linting an entire directory, check out (what else!)
[`tldr tldrl`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldrl.md).

Your client may be able to preview a page locally using the `--render` flag:

```
tldr --render {{page.md}}
```

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
- For any reference to paths to files or directories, use the format `{{path/to/<placeholder>}}`.
  For example, `ln -s {{path/to/file}} {{path/to/symlink}}`.
  In case of a possible reference both to a file or a directory, use `{{path/to/file_or_directory}}`
- Follow the `{{path/to/<placeholder>}}` convention for all path-related commands,
  except when the file location is implicit.
#### Extensions
- If a particular extension is expected for the file, append it.
  For example, `unrar x {{compressed.rar}}`.
- In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
  For instance, in find.md's example "Find files by extension" (`find {{root_path}} -name '{{*.ext}}'`)
  using `{{*.ext}}` explains the command without being unnecessarily specific;
  But in a command like `wc -l {{file}}` using `{{file}}` (without extension) is sufficient.

### Special cases
- If a command performs irreversible changes to a file system or devices,
  write every example in a way that they cannot be thoughtlessly copy-pasted.
  For example, instead of `ddrescue --force --no-scrape /dev/sda /dev/sdb`
  write `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`
  and use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.
- If a command can take a variable number of arguments, write `{{arg1 arg2 ...}}`.
  If one of multiple options is possible, write it as `{{either|or}}`.

In general, tokens should make it as intuitive as possible
to figure out how to use the command and fill it in with values.

Technical wording on description lines should use the `backtick` syntax.
Use backticks on the following:

- Paths, ex. `package.json`, `/etc/package.json`.
- Extensions, ex. `.dll`.
- Commands, ex. `ls`.

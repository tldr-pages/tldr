# Style Guide

This page lists specific formatting instructions for tldr pages.

## Layout

The basic format of each page should match the following template:

```
# command-name

> Short, snappy description.
> Preferably one line; two are acceptable if necessary.

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
[`tldr tldrl`](https://github.com/tldr-pages/tldr/blob/master/pages/common/tldrl.md)

If you're using the Node.js client of `tldr`, you can preview a page locally using the `-f` flag (aka `--render`):

```
tldr -f {{page.md}}
```

## Token syntax

User-provided values should use the `{{token}}` syntax
in order to allow `tldr` clients to highlight them.

Keep the following guidelines in mind when choosing tokens:

1. Use short but descriptive tokens,
   ex. `{{source_file}}` or `{{wallet.txt}}`.
2. Use [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) for multi-word tokens.
3. For any reference to paths to files or directories, use the format `{{path/to/<placeholder>}}`.
   For example, `ln -s {{path/to/file}} {{path/to/symlink}}`.
   In case of a possible reference both to a file or a directory, use `{{path/to/file_or_directory}}`
4. Follow the `{{path/to/<placeholder>}}` convention for all path-related commands, except when the
   file location is implicit.
5. If a command expects the file to have a particular extension, use it.
   For example, `unrar x {{compressed.rar}}`.
   In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
   For instance, in find.md's example "Find files by extension" (`find {{root_path}} -name '{{*.ext}}'`)
   using `{{*.ext}}` explains the command without being unnecessarily specific;
   But in a command like `wc -l {{file}}`, using `{{file}}` (without extension) is sufficient.
6. If the example is clearer with an actual value rather than a generic placeholder, use the actual value.
   For example, use `iostat {{2}}` rather than `iostat {{interval_in_secs}}`.

In general, tokens should make it as intuitive as possible
to figure out how to use the command and fill it in with values.

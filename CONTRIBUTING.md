# Contributing

[![Gitter chat][gitter-image]][gitter-url]
[![Merged PRs][prs-merged-image]][prs-merged-url]
[![Issue stats][issuestats-image]][issuestats-url]
[![GitHub contributors][contributors-image]][contributors-url]
[![CLA assistant][cla-assistant-image]][cla-assistant-url]
[![license][license-image]][license-url]

[gitter-url]: https://gitter.im/tldr-pages/tldr
[gitter-image]: https://badges.gitter.im/tldr-pages/tldr.svg
[prs-merged-url]: https://github.com/tldr-pages/tldr/pulls?q=is:pr+is:merged
[prs-merged-image]: https://img.shields.io/github/issues-pr-closed-raw/tldr-pages/tldr.svg?label=merged+PRs
[issuestats-url]: http://isitmaintained.com/project/tldr-pages/tldr
[issuestats-image]: http://isitmaintained.com/badge/resolution/tldr-pages/tldr.svg
[contributors-url]: https://github.com/tldr-pages/tldr/graphs/contributors
[contributors-image]: https://img.shields.io/github/contributors/tldr-pages/tldr.svg
[cla-assistant-url]: https://cla-assistant.io/tldr-pages/tldr
[cla-assistant-image]: https://cla-assistant.io/readme/badge/tldr-pages/tldr
[license-url]: https://github.com/tldr-pages/tldr/blob/master/LICENSE.md
[license-image]: https://img.shields.io/github/license/tldr-pages/tldr.svg

Contributions are most welcome! All `tldr` pages are stored in Markdown right here on GitHub.
Just open an issue or send a pull request and we'll incorporate it as soon as possible.
To get started, sign the [Contributor License Agreement](https://cla-assistant.io/tldr-pages/tldr).

*Note*: when submitting a new command, don't forget to check if there's already a pull request in progress for it.

## Guidelines

The basic format of a `tldr` page is a set of concrete usage examples.
Here are a few guidelines to get started:

1. Try to keep pages at around 5 examples. Pages can be longer if needed, but don't exceed 8 examples.
   Remember, it's OK if the page doesn't cover everything; that's what `man` is for.
2. When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
   For example, commands that require `sudo` should include it directly in the examples.
3. Try to incorporate the spelled-out version of single-letter options in the example's description.
   The goal is to allow people to *understand* the syntax of the commands, not just *memorize* it.
4. Introduce options gradually, starting with the simplest command invocations,
   and using more complex examples progressively.
5. Focus on details specific to the command, and avoid explaining general UNIX concepts that could apply to any command
   (ex: relative/absolute paths, glob patterns/wildcards, special character escaping...).

The best way to be consistent is to have a look at a few existing pages :).

## Markdown format

The format of each page should match the following:

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

### Token syntax

User-provided values should use the `{{token}}` syntax in order to allow `tldr` clients to highlight them.
Use [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) for multi-word tokens.

Keep the following guidelines in mind when choosing token names:

1. Use short but descriptive values for the tokens,
   ex. `{{source_file}}` or `{{wallet.txt}}`.
   
2. If the example is clearer with an actual value rather than a generic placeholder, use the actual value.
   For example, use `iostat {{2}}` rather than `iostat {{interval_in_secs}}`.

3. For any reference to paths to files or folders, use the format `{{path/to/<placeholder>}}`.
   For example, `ln -s {{path/to/file}} {{path/to/symlink}}`.
   In case of a possible reference both to a file or a folder, use `{{path/to/file_or_folder}}`
   
4. Follow the `{{path/to/<placeholder>}}` convention when there is a path-related command,
  except when the file location is implicit.

5. If a command expects the file to have a particular extension, use it.
   For example, `unrar x {{compressed.rar}}`.
   In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
   For instance, in find.md's example "Find files by extension" (`find {{root_path}} -name '{{*.ext}}'`)
   using `{{*.ext}}` explains the command without being unnecessarily specific;
   But in a command like `wc -l {{file}}`, using `{{file}}` (without extension) is sufficient.


These are all guidelines, not strict rules.
In general, tokens should make it as intuitive as possible
to figure out how to use the command and fill it in with values.
Use proper judgement, keeping simplicity and user-friendliness as the top priority.

## Submitting a pull request

For submitting changes, you can use whatever workflow you're more comfortable with.

### Using Github's web interface

The easiest way to submit a change is to just edit the page directly on the Github interface.
Check out the step-by-step instructions (with screenshots) on
[Github Help](https://help.github.com/articles/editing-files-in-another-user-s-repository/).

### Using the command line

Alternatively, you can do most of the process using the command line:

- fork the repository on the github web interface

- clone your fork locally:  
  `git clone https://github.com/{{your_username}}/tldr.git && cd tldr`

- create a feature branch, e.g. named after the command you plan to edit:  
  `git checkout -b {{branch_name}}`

- make your changes (edit existing files or create a new one)

- commit the changes:  
  `git commit --all -m "{{commit_message}}"`

- push to your fork:  
  `git push`

- go to the github page for your fork and click the green pull request button.

Please send only related changes in the same pull request.
Typically a pull request will include changes in a single file.

### Commit message

For the commit message, use the following format:

    <command>: type of change

Examples:
  - `ls: add page`
  - `cat: fix typo`
  - `git-push: add --force example`

## Licensing

`tldr` is licensed under the [MIT license](https://github.com/tldr-pages/tldr/blob/master/LICENSE.md).

Any contributions to this project are governed by the
[Contributor License Agreement](https://cla-assistant.io/tldr-pages/tldr).

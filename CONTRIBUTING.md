# Contributing

- Your favourite command isn't covered?
- You can think of more examples?

Contribution are most welcome! All `tldr` pages are stored in Markdown right here on GitHub. Just open an issue or send a pull request and we'll merge it as soon as possible.

*Note: when submitting a new command, don't forget to check if there's already a pull request in progress.*

## Setup

When setting up a brand new fork, run `make setup` to install the git pre-commit hook that will rebuild the index every time you commit your changes. You can also rebuild it manually by running `make index`. The script requires Ruby to run. Make sure you have the index in place as we will need it as part of your commit in order to pull in your changes.

## Guidelines

Note that `tldr` is focused on concrete examples.
Here's a few guidelines to get started:

- Focus on the 5 or 6 most common usages. It's OK if the page doesn't cover everything; that's what `man` is for.
- When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
- Try to incorporate the spelled-out version of single-letter options in the example's description.
- Introduce options gradually, starting with the simplest commands and using more complex examples progressively.
- Use short but descriptive values for the tokens, ex. `{{source_file}}` or `{{wallet.txt}}`.
- Be specific: avoid explaining general UNIX concepts that could apply to any command (ex: relative/absolute paths, brace expansion, character escaping...)

The best way to be consistent is to have a look at a few existing pages :)

## Markdown format

The format of each page should match the following:

```
# command-name

> Short description
> Max 1 or 2 lines

- example description

`command -opt1 -opt2 -arg1 {{arg_value}}`

- example description

`command -opt1 -opt2`
```

User-provided values should use the `{{token}}` syntax, to allow clients to highlight them. For example: `tar cf {{file}}`

One of the reasons for this format is that it's well suited for command-line clients that need to extract a single description/example.

---------------------------------------

**Footnote:** tldr is under MIT license.

You're free to modify or redistribute the content. That being said, but why not contribute over here? :) Say if you wanted to have `tldr` pages in `groff` format, why not have a client that uses [pandoc](http://johnmacfarlane.net/pandoc/) and periodically updates straight from this repo?

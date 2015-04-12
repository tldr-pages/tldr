# Contributing

- Your favourite command isn't covered?
- You can think of more examples?

Contribution are most welcome! All `tldr` pages are stored in Markdown right here on GitHub. Just open an issue or send a pull request and we'll merge it as soon as possible.

*Note: when submitting a new command, don't forget to check if there's already a pull request in progress.*

## Setup

When setting up a brand new fork, run `make setup` to install the git pre-commit hook that will rebuild the index every time you commit your changes. You can also rebuild it manually by running `make index`. The script requires Ruby to run. Make sure you have the index in place as we will need it as part of your commit in order to pull in your changes.

## Guidelines

Note that `tldr` is focussed on concrete examples.
Here's a few guidelines to get started:

- Focus on the 5 or 6 most common usages
- When in doubt, keep new command-line users in mind
- It's OK if the page doesn't cover everything, that's what `man` is for

Token formatting:

- Highlight user-provided values using the `{{token}}` syntax, for example `tar cf {{file}}`
- For consistency in the tokens, use plain text descriptions (`{{source_file}}`) or short descriptive examples (`{{wallet.txt}}`)

Common pitfalls / "donts"

- Don't try to cover all possible examples, or combinations of flags (often, this is not possible without looking like `man`)
- Don't explain general UNIX concepts that could apply to any command (ex: relative/absolute paths, brace expansion...)
- Avoid catch-all examples like `tar {{options}}`
- Don't group options as a trick to keep pages short (`tar {{c or x}}`)

The best way to be consistent is to have a look at a few existing pages :)

## Markdown format

For now, the format of each page has to match the following:

```
# command-name

> Short description
> Max 1 or 2 lines

- example description

`command -arg1 -arg2`

- example description

`command -arg1 -arg2`
```

Eventually we might relax the format to accept any Markdown, but for now this has the advantage of adding some consitency between all pages, and making sure we focus on concrete examples rather than lengthy explanation of the different flags.

The current format also works well for command-line clients that need to extract a single description/example.

---------------------------------------

**Footnote:** tldr is under MIT license.

You're free to modify or redistribute the content. That being said, but why not contribute over here? :) Say if you wanted to have `tldr` pages in `groff` format, why not have a client that uses [pandoc](http://johnmacfarlane.net/pandoc/) and periodically updates straight from this repo?

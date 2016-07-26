# Contributing

Contributions are most welcome! All `tldr` pages are stored in Markdown right here on GitHub.
Just open an issue or send a pull request and we'll incorporate it as soon as possible.

*Note*: when submitting a new command, don't forget to check if there's already a pull request in progress for it.

## Guidelines

The basic format of a `tldr` page is a set of concrete usage examples.
Here are a few guidelines to get started:

1. Focus on the 5 or 6 most common usages. It's OK if the page doesn't cover everything; that's what `man` is for.
2. When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
3. Try to incorporate the spelled-out version of single-letter options in the example's description.
   The goal is to allow people to *understand* the syntax of the commands, not just *memorize* it.
4. Introduce options gradually, starting with the simplest commands and using more complex examples progressively.
5. Use short but descriptive values for the tokens, ex. `{{source_file}}` or `{{wallet.txt}}`.
6. Focus on details specific to the command, and avoid explaining general UNIX concepts that could apply to any command
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

We actually have a linter/formatter that enforces our format.
It is run automatically on every pull request,
but you may install it to test your contributions locally before submitting them:

```
npm install tldr-lint
tldrl -f {{page.md}}
```

For other ways to use `tldrl`, such as linting an entire directory, check out (what else!)
[`tldr tldrl`](https://github.com/tldr-pages/tldr/blob/master/pages/common/tldrl.md)

### Token syntax
User-provided values should use the `{{token}}` syntax in order to allow clients
to highlight them. 

Some examples: 
- `tar cf {{file}}`
- `ln -s {{path/to/original/file}} {{path/to/link}}`
- `mysql {{database_name}}`
- `unrar x {{compressed.rar}}`

In short, make it as intuitive as possible
for the user to figure out how to use the command
and fill it in with values.

Stick to [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) where possible.
In some situations a command works with typical file extensions
(like the `unrar` example above);
you are encouraged to add these for demonstration.

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
  - `uname: fix -a example`

## Licensing

`tldr` is licensed under the [MIT license](https://github.com/tldr-pages/tldr/blob/master/LICENSE.md).

**IMPORTANT**: By submitting a patch, you agree to license your work
under the same license as that used by the project.

You're free to modify or redistribute the content.
That being said, but why not contribute over here? :)
Say if you wanted to have `tldr` pages in `groff` format,
why not have a client that uses [pandoc](http://johnmacfarlane.net/pandoc/)
and periodically updates straight from this repo?

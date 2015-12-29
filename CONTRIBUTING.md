# Contributing

Contribution are most welcome! All `tldr` pages are stored in Markdown right here on GitHub. Just open an issue or send a pull request and we'll merge it as soon as possible.

*Note*: when submitting a new command, don't forget to check if there's already a pull request in progress.

## Guidelines

Note that `tldr` is focused on concrete examples.
Here's a few guidelines to get started:

1. Focus on the 5 or 6 most common usages. It's OK if the page doesn't cover everything; that's what `man` is for.
2. When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
3. Try to incorporate the spelled-out version of single-letter options in the example's description.
4. Introduce options gradually, starting with the simplest commands and using more complex examples progressively.
5. Use short but descriptive values for the tokens, ex. `{{source_file}}` or `{{wallet.txt}}`.
6. Be specific: avoid explaining general UNIX concepts that could apply to any command (ex: relative/absolute paths, brace expansion, character escaping...)

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

## Submitting a pull request

TL;DR: fork, `make setup`, feature branch, commit, push, pull request.

Detailed explanation:

1. [Fork](http://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/tldr
   # Navigate to the newly cloned directory
   cd tldr
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/tldr-pages/tldr
   ```

2. Setup Ruby, Rubygems, bundler, Git pre-commit hooks with Markdown linter.

   ```bash
   # Assuming Ruby is set up
   # Install bundler Ruby gem
   gem install bundler
   make setup
   ```

3. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout master
   git pull upstream master
   ```

4. Create a new topic branch (sometimes they are called feature branches) off
   the main project development branch:

   ```bash
   git checkout -b <topic-branch-name>
   ```

5. Run `make lint` to check that your page(s) are correct.

6. Please use the following commit message format: 
   `<command>: type of change`.

   Examples:

   - `ls: add page`
   - `cat: fix typo`
   - `git-push: add --force example`
   - `uname: fix -a example`

7. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

8. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description.

9. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.
   In most cases it is better to squash commits before submitting a pull request.

10. If you are asked to amend your changes before they can be merged in, please
   use `git commit --amend` and force push to your remote feature branch.
   You may also be asked to squash commits.


## Licensing

`tldr` is under [MIT license](https://github.com/tldr-pages/tldr/blob/master/LICENSE.md).

**IMPORTANT**: By submitting a patch, you agree to license your work under the
same license as that used by the project.

You're free to modify or redistribute the content. That being said, but why not contribute over here? :) Say if you wanted to have `tldr` pages in `groff` format, why not have a client that uses [pandoc](http://johnmacfarlane.net/pandoc/) and periodically updates straight from this repo?

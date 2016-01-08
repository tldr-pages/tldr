# Contributing

Contribution are most welcome! All `tldr` pages are stored in Markdown right here on GitHub. Just open an issue or send a pull request and we'll merge it as soon as possible.

*Note*: when submitting a new command, don't forget to check if there's already a pull request in progress.

## Guidelines

Note that `tldr` is focused on concrete examples.
Here are a few guidelines to get started:

1. Focus on the 5 or 6 most common usages. It's OK if the page doesn't cover everything; that's what `man` is for.
2. When in doubt, keep new command-line users in mind. Err on the side of clarity rather than terseness.
3. Try to incorporate the spelled-out version of single-letter options in the example's description.
4. Introduce options gradually, starting with the simplest commands and using more complex examples progressively.
5. Use short but descriptive values for the tokens, ex. `{{source_file}}` or `{{wallet.txt}}`.
6. Be specific: avoid explaining general UNIX concepts that could apply to any command (ex: relative/absolute paths, brace expansion, character escaping...).

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

### Token Syntax
User-provided values should use the `{{token}}` syntax in order to allow clients
to highlight them. 

Some examples: 
- `tar cf {{file}}`
- `ln -s {{path/to/original/file}} {{path/to/link}}`
- `mysql {{database_name}}`
- `unrar x {{compressed.rar}}`

In short, make it as intuitive as possible for the user to figure out
how to use the command and fill it in with values.
Stick to [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) where possible.
In some situations a command works with typical file extensions
(like the `unrar` example above); you are encouraged to add these for demonstration.

One of the reasons for this format is that it's well suited for command-line
clients that need to extract a single description/example.

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

5. Run `make lint` to check that your page(s) are correct. Try to run the commands you are describing to ensure the syntax is correct.

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
    
    If page is not about a standard Unix/Linux tool, please include a link to the tool home page.
    
    If you are changing something non-trivial, not just adding a page for a new tool, please describe why you are doing this.

9. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.
   
   If you are not familiar with `git rebase`, it might be helpful to check out these video tutorials:
   - [Git Rebase: squash last commits](https://www.youtube.com/watch?v=qh9KtjfjzCU)
   - [Learning Git Tutorial: Interactive Rebasing](https://www.youtube.com/watch?v=NW46XmvJh5Q)
   
   In most cases it is better to squash commits before submitting a pull request.

10. If you do not want to do a rebasing, you can overwrite your last commit in pull request, while you have only a single commit. You can achieve this with `git commit --amend` command.

   ```bash
   # When you are on topic branch of your pull request
   # Fix your files
   
   git add .              # Register edited files
   git commit --amend     # Do amended commit
   git push --force       # Overwrite your branch
   ```


## Licensing

`tldr` is under [MIT license](https://github.com/tldr-pages/tldr/blob/master/LICENSE.md).

**IMPORTANT**: By submitting a patch, you agree to license your work under the
same license as that used by the project.

You're free to modify or redistribute the content. That being said, but why not contribute over here? :) Say if you wanted to have `tldr` pages in `groff` format, why not have a client that uses [pandoc](http://johnmacfarlane.net/pandoc/) and periodically updates straight from this repo?

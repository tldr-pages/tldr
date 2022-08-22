# Quick start

This page quickly describes `tldr` page syntax with several examples. For strict rules please follow our [style guide](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/style-guide.md).

## Simplest example

Here is an example of page describing `pwd` command:

```md
# pwd

> Print name of current/working directory.
> More information: <https://www.gnu.org/software/coreutils/pwd>.

- Print the current directory:

`pwd`

- Print the current directory, and resolve all symlinks (i.e. show the "physical" path):

`pwd --physical`

- Print the current logical directory:

`pwd --logical`
```

Although `tldr` pages use Markdown syntax, we should note some conventions that we follow:

- The first line is a header of the page.
- Lines beginning with a `>` contain the short command description (in an imperative mood) and link the GNU Core Utilities (coreutils) `pwd` page.
- Each command placed in backticks have a description above it (in an imperative mood) beginning with a `-`.
- Here we have 3 command examples but more complex commands can have longer pages. As we can't support very long pages we restricted example count upt to 8.

## More complex example

Some commands allow or require arguments such as [caja](https://manned.org/caja).

```
# caja

> Manage files and directories in MATE desktop environment.
> More information: <https://manned.org/caja>.

- Open the current user home directory:

`caja`

- Open specific directories in separate windows:

`caja {{path/to/directory1 path/to/directory2 ...}}`

- Open specific directories in tabs:

`caja --tabs {{path/to/directory1 path/to/directory2 ...}}`

- Open a directory with a specific window size:

`caja --geometry={{600}}x{{400}} {{path/to/directory}}`

- Close all windows:

`caja --quit`
```

Note how we describe what is expected as the command argument via double curly braces.

- Everything between `{{` and `}}` is a placeholder.
- We can write almost everything inside it but by our convention we use:
  - `{{path/to/directoryX}}` for path to some directory obviously
  - `...` before `}}` when there can be any argument count and we don't mind what
  - concreete values such as `{{5}}` when it's easiear to understand command
- The second command example uses ellipsis to show that user can pass any directory count to this program.
- Note that in the same example we duplicate `path/to/directory` with just another digit at the end. This is also our convention.
  And we use it with `...`.


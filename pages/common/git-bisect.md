# git bisect

> Use binary search to find the commit that introduced a bug.
> Git automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit.
> More information: <https://git-scm.com/docs/git-bisect>.

- Start a bisect session on a commit range bounded by a known buggy commit, and a known clean (typically older) one:

`git bisect start {{bad_commit}} {{good_commit}}`

- For each commit that `git bisect` selects, mark it as "bad" or "good" after testing it for the issue:

`git bisect {{good|bad}}`

- End the bisect session and return to the previous branch:

`git bisect reset`

- Skip a commit during a bisect (e.g. one that fails the tests due to a different issue):

`git bisect skip`

- Start a bisect session considering only commits that modify a specific file or directory:

`git bisect start {{bad_commit}} {{good_commit}} -- {{path/to/file_or_directory}}`

- Automate the bisect process using a test script that `exit`s with 0 for "good" and non-zero for "bad" (script arguments are optional):

`git bisect run {{path/to/test_script}} {{script_arguments}}`

- Display a log of what has been done so far:

`git bisect log`

- Show remaining candidate commits to be checked:

`git bisect visualize`

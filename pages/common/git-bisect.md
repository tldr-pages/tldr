# git bisect

> Use binary search to find the commit that introduced a bug.
> Git automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit.

- Start a bisect section by passing a known good commit and a known bad commit:

`git bisect start {{bad_commit}} {{good_commit}}`

- For each commit that `git bisect` selects, mark it as "bad" or "good":

`git bisect {{good|bad}}`

- After `git bisect` pinpoints the faulty commit, end the bisect session and return to the previous branch:

`git bisect reset`

- Skip a commit during a bisect (e.g. one that causes a broken build due to another issue):

`git bisect skip`


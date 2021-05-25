# git commit-graph

> Write and verify Git commit-graph files.
> More information: <https://git-scm.com/docs/git-commit-graph>.

- Write a commit-graph file for the packed commits in the repository's local `.git` directory:

`git commit-graph write`

- Write a commit-graph file containing all reachable commits:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Write a commit-graph file containing all commits in the current commit-graph file along with those reachable from `HEAD`:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`

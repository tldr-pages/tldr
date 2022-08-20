# vgrep

> A user friendly pager for grep.
> See also: `ugrep`, `rg`.
> More information: <https://github.com/vrothberg/vgrep>.

- Recursively search the current directory for a pattern and cache it:

`vgrep {{search_pattern}}`

- Display the contents of the cache:

`vgrep`

- Open the "4th" match from the cache in the default editor:

`vgrep --show {{4}}`

- Display a context of "3" lines for each match in the cache:

`vgrep --show=context{{3}}`

- Display the number of matches for each directory in the tree:

`vgrep --show=tree`

- Display the number of matches for each file in the tree:

`vgrep --show=files`

- Start an interactive shell with cached matches:

`vgrep --interactive`

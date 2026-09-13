# git interpret-trailers

> Add or parse structured trailer lines (like `Signed-off-by:` or `Reviewed-by:`) at the end of a commit message.
> More information: <https://git-scm.com/docs/git-interpret-trailers>.

- Add a trailer to a commit message file and print the result:

`git interpret-trailers --trailer "{{key}}: {{value}}" {{path/to/file}}`

- Add a trailer to a commit message file, modifying it in place:

`git interpret-trailers --in-place --trailer "{{key}}: {{value}}" {{path/to/file}}`

- Parse and print only the trailers already present in a commit message file:

`git interpret-trailers --parse {{path/to/file}}`

- Remove trailers that have an empty value from a commit message file:

`git interpret-trailers --trim-empty {{path/to/file}}`

- Add a trailer to the message of an existing commit, printing the result without modifying the commit:

`git show --no-patch --format=%B {{commit_hash}} | git interpret-trailers --trailer "{{key}}: {{value}}"`

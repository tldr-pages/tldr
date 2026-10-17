# git interpret-trailers

> Add or parse structured information (trailers) at the end of commit messages.
> More information: <https://git-scm.com/docs/git-interpret-trailers>.

- Add a trailer to a commit message file and print the result to `stdout`:

`git interpret-trailers --trailer "{{key}}: {{value}}" {{path/to/message_file}}`

- Add multiple trailers:

`git interpret-trailers --trailer "{{key1}}: {{value1}}" --trailer "{{key2}}: {{value2}}" {{path/to/message_file}}`

- Add a trailer and edit the message file in place:

`git interpret-trailers --in-place --trailer "{{key}}: {{value}}" {{path/to/message_file}}`

- Add a trailer only if the same key and value pair is not already present:

`git interpret-trailers --if-exists addIfDifferent --trailer "{{key}}: {{value}}" {{path/to/message_file}}`

- Add a trailer before the existing trailers instead of after them:

`git interpret-trailers --where start --trailer "{{key}}: {{value}}" {{path/to/message_file}}`

- Print only the trailers from the message of the latest commit:

`git log --max-count 1 --format=%B | git interpret-trailers --parse`

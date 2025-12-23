# rcsdiff

> Compare RCS revisions (show differences between revisions in RCS files).
> See also: `ci`, `co`, `rcs`, `rlog`.
> More information: <https://manned.org/rcsdiff>.

- Compare the working file with the latest revision:

`rcsdiff {{path/to/file}}`

- Compare the working file with a specific revision:

`rcsdiff -r{{revision}} {{path/to/file}}`

- Compare two specific revisions of a file:

`rcsdiff -r{{revision1}} -r{{revision2}} {{path/to/file}}`

- Show differences in unified format:

`rcsdiff -u {{path/to/file}}`

- Show differences with context lines:

`rcsdiff -c {{path/to/file}}`

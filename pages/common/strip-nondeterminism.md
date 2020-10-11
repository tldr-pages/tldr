# strip-nondeterminism

> A tool to remove non-deterministic information (e.g. timestamps) from files.

- Strip non-deterministic information from a file:

`strip-nondeterminism {{file}}` 

- Strip nondeterministic information from a file while manually specifying the file type:

`strip-nondeterminism --type {{ar|gzip|jar|zip}} {{file}}`

- Strip nondeterministic information from a file; instead of removing timestamps set them to the specified UNIX timestamp:

`strip-nondeterminism --timestamp {{unix-timestamp}} {{file}}`

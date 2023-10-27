# rmlint

> Find space waste and other broken things on your filesystem.
> More information: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Check directories for duplicated, empty and broken files:

`rmlint {{path/to/directory1 path/to/directory2 ...}}`

- Check for space wasters, preferably keeping files in tagged directories (after the double slash):

`rmlint {{path/to/directory}} // {{path/to/original_directory}}`

- Check for space wasters, keeping everything in the untagged directories:

`rmlint --keep-all-untagged {{path/to/directory}} // {{path/to/original_directory}}`

- Delete duplicate files found by an execution of `rmlint`:

`./rmlint.sh`

- Find duplicate directory trees:

`rmlint --merge-directories {{path/to/directory}}`

- Mark files at lower path [d]epth as originals, on tie choose shorter [l]ength:

`rmlint --rank-by={{dl}} {{path/to/directory}}`

- Find only duplicates that have the same filename in addition to the same contents:

`rmlint --match-basename {{path/to/directory}}`

- Find only duplicates that have the same extension in addition to the same contents:

`rmlint --match-extension {{path/to/directory}}`

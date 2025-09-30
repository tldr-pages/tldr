# tag

> Edit tags on Mac OS X files (10.9 Mavericks and above).
> More information: <https://github.com/jdberry/tag/>.

- Add tags to a file:

`tag --add {{tag_name1,tag_name2,...}} {{path/to/file}}`

- Remove a tag:

`tag --remove {{tag_name}} {{path/to/file}}`

- Remove all tags from a file:

`tag --remove \* {{path/to/file}}`

- Show all files with a given tag:

`tag --match {{tag_name}}`

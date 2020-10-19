# ack

> A search tool like grep, optimized for programmers.
> More information: <https://beyondgrep.com/documentation/>.

- Find files containing "foo":

`ack {{foo}}`

- Find files of a specific type:

`ack --ruby {{foo}}`

- Count the total number of matches for the term "foo":

`ack -ch {{foo}}`

- Show the file names containing "foo" and number of matches in each file:

`ack -cl {{foo}}`

- Search a file for a specified string:

`ack bar "{{foo bar}}" {{path/to/file}}`

- Search a file for the specified regex pattern:

`ack bar "{{[bB]ar \d+}}" {{path/to/file}}`

- List all valid types:

`ack --help-types`

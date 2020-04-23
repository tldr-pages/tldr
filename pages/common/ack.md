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

- Search file "my_file" for string "foo bar"

`ack bar "{{foo bar}}" {{my_file}}`

- Search file "my_file" for regex pattern "[bB]ar \d+"

`ack bar "{{[bB]ar \d+}}" {{my_file}}`

- List all valid types:

`ack --help=types`

- Search file "my_file" for string "foo bar"

`ack bar "{{foo bar}}" {{my_file}}`

- Search file "my_file" for regex pattern "[bB]ar \d+"

`ack bar "{{[bB]ar \d+}}" {{my_file}}`

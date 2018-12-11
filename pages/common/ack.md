# ack

> A search tool like grep, optimized for programmers.

- Find files containing "foo":

`ack {{foo}}`

- Find files in a specific language:

`ack --ruby {{each_with_object}}`

- Count the total number of matches for the term "foo":

`ack -ch {{foo}}`

- Show the file names containing "foo" and number of matches in each file:

`ack -cl {{foo}}`

- Search file "my_file" for string "foo bar":

`ack bar "{{foo bar}}" {{my_file}}`

- Search file "my_file" for regex pattern "[bB]ar \d+":

`ack bar "{{[bB]ar \d+}}" {{my_file}}`

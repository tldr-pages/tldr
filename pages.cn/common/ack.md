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

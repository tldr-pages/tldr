# tee

> Read from standard input and write to standard output and files (or commands).

- Copy standard input to each FILE, and also to standard output:

`echo "example" | tee {{FILE}}`

- Append to the given FILEs, do not overwrite:

`echo "example" | tee -a {{FILE}}`

- Print standard input to the terminal, and also pipe it into another program for further processing:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:

`echo "example" | tee >(xargs mkdir) >(wc -c)`

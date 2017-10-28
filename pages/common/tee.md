# tee

> Read from standard input and write to standard output and files (or commands).

- Copy standard input to each FILE, and also to standard output:

`echo "example" | tee {{FILE}}`

- Append to the given FILEs, do not overwrite:

`echo "example" | tee -a {{FILE}}`

- Create a folder called "example", count the number of characters in "example and write "example" to the terminal:

`echo "example" | tee >(xargs mkdir) >(wc -c)`

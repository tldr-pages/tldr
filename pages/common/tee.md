# tee

> Read from standard input and write to standard output and files (or commands).

- Copy standard input to each FILE, and also to standard output:

`echo "example" | tee {{FILE}}`

- Append to the given FILEs, do not overwrite:

`echo "example" | tee -a {{FILE}}`

- Create a folder called "example", print "example" and write "example" to the specified file:

`echo "example" | tee >(xargs mkdir) >(cat) >{{path/to/file}}`

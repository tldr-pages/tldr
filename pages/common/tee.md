# tee

> Read from standard input and write to standard output and files.

- Copy standard input to each FILE, and also to standard output:

`echo "example" | tee {{FILE}}`

- Append to the given FILEs, do not overwrite:

`echo "example" | tee -a {{FILE}}`

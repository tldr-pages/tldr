# awk

> A versatile programming language for working on files.

- Print the fifth column (a.k.a. field) in a space-separated file:

`awk '{print $5}' {{filename}}`

- Print the second column of the lines containing "something" in a space-separated file:

`awk '/{{something}}/ {print $2}' {{filename}}`

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:

`awk -F ',' '{print $NF}' {{filename}}`

- Sum the values in the first column of a file and print the total:

`awk '{s+=$1} END {print s}' {{filename}}`

- Sum the values in the first column and pretty-print the values and then the total:

`awk '{s+=$1; print $1} END {print "--------"; print s}' {{filename}}`

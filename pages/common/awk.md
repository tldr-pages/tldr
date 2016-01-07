# awk

> A versatile programming language for working on files.

- Print the fifth column in a space separated file:

`awk '{print $5}' {{filename}}`

- Print the third column in a comma separated file:

`awk -F ',' '{print $3}' {{filename}}`

- Sum the values in the first column and print the total:

`awk '{s+=$1} END {print s}' {{filename}}`

- Sum the values in the first column and pretty-print the values and then the total:

`awk '{s+=$1; print $1} END {print "--------"; print s}' {{filename}}`

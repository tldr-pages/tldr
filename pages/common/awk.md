# awk

> A versatile programming language for working on files.
> More information: <https://github.com/onetrueawk/awk>.

- Print the fifth column (a.k.a. field) in a space-separated file:

`awk '{print $5}' {{filename}}`

- Print the second column of the lines containing "foo" in a space-separated file:

`awk '/{{foo}}/ {print $2}' {{filename}}`

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:

`awk -F ',' '{print $NF}' {{filename}}`

- Sum the values in the first column of a file and print the total:

`awk '{s+=$1} END {print s}' {{filename}}`

- Print every third line starting from the first line:

`awk 'NR%3==1' {{filename}}`

- Print different values based on conditions:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{filename}}`

- Print all lines where the 10th column value equals the specified value :

`awk '($10 == value)'`

- Print all the lines which the 10th column value is between a min and a max :

`awk '($10 >= min_value && $10 <= max_value)'`

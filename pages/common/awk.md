# awk

> A versatile programming language for working on files.
> Note: Different implementations of AWK often make this a symlink of their binary.
> See also: `gawk`.
> More information: <https://github.com/onetrueawk/awk>.

- Print the fifth column (a.k.a. field) in a space-separated file:

`awk '{print $5}' {{path/to/file}}`

- Print the second column of the lines containing "foo" in a space-separated file:

`awk '/{{foo}}/ {print $2}' {{path/to/file}}`

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:

`awk -F ',' '{print $NF}' {{path/to/file}}`

- Sum the values in the first column of a file and print the total:

`awk '{s+=$1} END {print s}' {{path/to/file}}`

- Print every third line starting from the first line:

`awk 'NR%3==1' {{path/to/file}}`

- Print different values based on conditions:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{path/to/file}}`

- Print all the lines which the 10th column value is between a min and a max:

`awk '($10 >= {{min_value}} && $10 <= {{max_value}})'`

- Print table of users with UID >=1000 with header and formatted output, using colon as separator (`%-20s` mean: 20 left-align string characters, `%6s` means: 6 right-align string characters):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`

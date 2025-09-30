# gawk

> GNU version of awk, a versatile programming language for working on files.
> See also: `awk`.
> More information: <https://www.gnu.org/software/gawk/manual/gawk.html>.

- Print the fifth column (a.k.a. field) in a space-separated file:

`gawk '{print $5}' {{path/to/file}}`

- Print the second column of the lines containing "foo" in a space-separated file:

`gawk '/{{foo}}/ {print $2}' {{path/to/file}}`

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:

`gawk {{[-F|--field-separator]}} ',' '{print $NF}' {{path/to/file}}`

- Sum the values in the first column of a file and print the total:

`gawk '{s+=$1} END {print s}' {{path/to/file}}`

- Print every third line starting from the first line:

`gawk 'NR%3==1' {{path/to/file}}`

- Print different values based on conditions:

`gawk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{path/to/file}}`

- Print all the lines which the 10th column value is between a min and a max:

`gawk '($10 >= {{min_value}} && $10 <= {{max_value}})'`

- Print table of users with UID >=1000 with header and formatted output, using colon as separator (`%-20s` mean: 20 left-align string characters, `%6s` means: 6 right-align string characters):

`gawk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`

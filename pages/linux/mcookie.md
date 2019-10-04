# mcookie

> Generate a 128-bit random hexadecimal number.

- Generate random number:

`mcookie`

- Generate random number, use destination file as a seed for the randomness:

`mcookie -f {{path/to/file1}} -f {{path/to/file2}}`

- Generate random number, read specific number of bytes from destination file and use it as a seed for the randomness:

`mcookie -f {{path/to/file1}} -m {{number_of_bytes}} -f {{path/to/file2}} -m {{number_of_bytes}}`s

- Print the detials of the randomness such as origin and seed from each sources:

`mcookie -v`

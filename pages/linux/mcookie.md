# mcookie

> Generate a 128-bit random hexadecimal number.

- Generate random number:

`mcookie`

- Generate a random number, using the contents of a file as a seed for the randomness:

`mcookie -f {{path/to/file1}} -f {{path/to/file2}}`

- Generate a random number, using a specific number of bytes from a file as a seed for the randomness:

`mcookie -f {{path/to/file1}} -m {{number_of_bytes}} -f {{path/to/file2}} -m {{number_of_bytes}}`

- Print the detials of the randomness such as origin and seed from each sources:

`mcookie -v`

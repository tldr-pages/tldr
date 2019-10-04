# mcookie

> Generate a 128-bit random hexadecimal number.

- Generate a random number:

`mcookie`

- Generate a random number, using the contents of a file as a seed for the randomness:

`mcookie --file {{path/to/file1}} --file {{path/to/file2}}`

- Generate a random number, using a specific number of bytes from a file as a seed for the randomness:

`mcookie --file {{path/to/file1}} --max-size {{number_of_bytes}} --file {{path/to/file2}} --max-size {{number_of_bytes}}`

- Print the detials of the randomness such as origin and seed from each sources:

`mcookie --verbose`

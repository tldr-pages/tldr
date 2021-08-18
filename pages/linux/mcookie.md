# mcookie

> Generates random 128-bit hexadecimal numbers.
> More information: <https://manned.org/mcookie>.

- Generate a random number:

`mcookie`

- Generate a random number, using the contents of a file as a seed for the randomness:

`mcookie --file {{path/to/file}}`

- Generate a random number, using a specific number of bytes from a file as a seed for the randomness:

`mcookie --file {{path/to/file}} --max-size {{number_of_bytes}}`

- Print the details of the randomness used, such as the origin and seed for each source:

`mcookie --verbose`

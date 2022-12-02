# xxd

> Create a hexadecimal representation (hexdump) from a binary file, or vice-versa.
> More information: <https://manned.org/xxd>.

- Generate a hexdump from a binary file and display the output:

`xxd {{path/to/file}}`

- Generate a hexdump from a binary file and save it as a text file:

`xxd {{path/to/file}} {{path/to/file}}`

- Display a more compact output, replacing consecutive zeros (if any) with a star:

`xxd -a {{path/to/file}}`

- Display the output with 10 columns of one octet (byte) each:

`xxd -c {{10}} {{path/to/file}}`

- Display output only up to a length of 32 bytes:

`xxd -l {{32}} {{path/to/file}}`

- Display the output in plain mode, without any gaps between the columns:

`xxd -p {{path/to/file}}`

- Revert a plaintext hexdump back into binary, and save it as a binary file:

`xxd -r -p {{path/to/file}} {{path/to/file}}`

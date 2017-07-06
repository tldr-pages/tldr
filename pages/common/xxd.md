# xxd

> Create a hexdump from a binary file or vice-versa.

- Generate a hexdump from a binary file and display the output to console:

`xxd {{input_file}}`

- Send the hexdump output to a file:

`xxd {{input_file}} {{output_file}}`

- Format output in columns of 8 octets per line:

`xxd -c {{8}} {{input_file}}`

- Display in plain hex format without any gaps:

`xxd -p {{input_file}}`

- Revert a plaintext hex into binary and store it in an output file:

`xxd -r -p {{input_file}} {{output_file}}`

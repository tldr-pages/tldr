# uuencode

> Encode binary files into ASCII for transport via mediums that only support simple ASCII encoding.
> More information: <https://manned.org/uuencode>.

- Encode a file and print the result to stdout:

`uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Encode a file and and write the result to a file:

`uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Encode a file using Base64 instead of the default uuencode encoding and and write the result to a file:

`uuencode -m -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

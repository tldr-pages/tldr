# certutil

> A tool to manage and configure certificate information.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- Dump the configuration information or files:

`certutil {{filename}}`

- Encode a file in hexadecimal:

`certutil -encodehex {{path\to\input_file}} {{path\to\output_file}}`

- Encode a file to Base64:

`certutil -encode {{path\to\input_file}} {{path\to\output_file}}`

- Decode a Base64-encoded file:

`certutil -decode {{path\to\input_file}} {{path\to\output_file}}`

- Generate and display a cryptographic hash over a file:

`certutil -hashfile {{path\to\input_file}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`

# Binwalk

> Firmware Analysis Tool.
> More information: <https://github.com/ReFirmLabs/binwalk>.

- Scan a binary file:

`binwalk {{binary}}`

- Extract files from a binary specifying the output directory:

`binwalk --extract --directory {{output_directory}} {{binary}}`

- Recursively extract files from a binary limiting the recursion depth to 2:

`binwalk --extract --matryoshka --depth 2 {{binary}}`

- Extract files from a binary with the specified file signature:

`binwalk --dd 'png image:png' {{binary}}`

- Analyze entropy of a binary saving the plot as a PNG:

`binwalk --entropy --save {{binary}}`

- Combine entropy, signature and opcodes analysis in a single command:

`binwalk --entropy --signature --opcodes {{binary}}`

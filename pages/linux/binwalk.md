# binwalk

> Firmware Analysis Tool.
> More information: <https://github.com/ReFirmLabs/binwalk>.

- Scan a binary file:

`binwalk {{path/to/binary}}`

- Extract files from a binary, specifying the output directory:

`binwalk --extract --directory {{output_directory}} {{path/to/binary}}`

- Recursively extract files from a binary limiting the recursion depth to 2:

`binwalk --extract --matryoshka --depth {{2}} {{path/to/binary}}`

- Extract files from a binary with the specified file signature:

`binwalk --dd '{{png image:png}}' {{path/to/binary}}`

- Analyze the entropy of a binary, saving the plot with the same name as the binary and `.png` extension appended:

`binwalk --entropy --save {{path/to/binary}}`

- Combine entropy, signature and opcodes analysis in a single command:

`binwalk --entropy --signature --opcodes {{path/to/binary}}`

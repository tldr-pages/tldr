# mopac

> MOPAC (Molecular Orbital PACkage) is a semiempirical quantum chemistry program based on Dewar and Thiel's NDDO approximation.
> More information: <https://github.com/openmopac/mopac>.

- Perform calculations according to an input file (`.mop`, `.dat`, and `.arc`):

`mopac {{path/to/input_file}}`

- Minimal working example with HF that writes to the current directory and streams the output file:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail {{[-f|--follow]}} test.out`

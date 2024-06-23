# mopac

> MOPAC (Molecular Orbital PACkage) is a semiempirical quantum chemistry program based on Dewar and Thiel's NDDO approximation.
> More information: <http://openmopac.net/>.

- Perform calculations according to an input file (`.mop`, `.dat`, `.arc`):

`mopac {{input_file}}`

- Stream output file:

`tail -f {{path/to/output_file}}`

- Minimal working example with HF that writes to the current directory:

`echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop`

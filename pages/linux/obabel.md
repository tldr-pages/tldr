# obabel

> Translate chemistry-related data.
> More information: <https://openbabel.org/wiki/Main_Page>.

- Convert a .mol file to XYZ coordinates:

`obabel {{path/to/file.mol}} -O {{path/to/output_file.xyz}}`

- Convert a SMILES string to a 500x500 picture:

`obabel -:"{{SMILES}} -O {{path/to/output_file.png}} -xp 500`

- Convert a file of SMILES string to separate 3D .mol files:

`obabel {{path/to/file.smi}} -O {{path/to/output_file.mol}} --gen3D -m`

- Render multiple inputs into one picture:

`obabel {{path/to/file1 path/to/file2 ...}} -O {{path/to/output_file.png}}`

# pamfile

> Describe Netpbm (PAM or PNM) files.
> More information: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Describe the specified Netpbm files:

`pamfile {{path/to/file1 path/to/file2 ...}}`

- Describe every image in each input file (as opposed to only the first image in each file) in a machine-readable format:

`pamfile -allimages -machine {{path/to/file}}`

- Display a count on how many images the input files contain:

`pamfile -count {{path/to/file}}`

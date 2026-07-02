# qtgrace

> Display, plot, analyze 2D data.
> A Qt reimplementation of Grace (<https://plasma-gate.weizmann.ac.il/Grace/>), sharing its command-line interface.
> More information: <https://sourceforge.net/projects/qtgrace/>.

- Plot one or more data files, plotting only the first two columns in each file as X Y:

`qtgrace {{path/to/file1.dat path/to/file2.dat ...}}`

- Plot one or more data files, plotting all columns in each file as X Y1 Y2 ...:

`qtgrace {{-nxy path/to/file1.dat -nxy path/to/file2.dat ...}}`

- Plot one or more data files with a logarithmically scaled x-axis:

`qtgrace -log x {{path/to/file1.dat path/to/file2.dat ...}}`

- Plot a data file with a logarithmic scale on both axes, with data formatted as X Y DY:

`qtgrace -log xy -settype xydy {{path/to/file.dat}}`

- Display help:

`qtgrace -help`

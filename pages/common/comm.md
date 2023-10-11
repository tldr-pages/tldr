# comm

> Select or reject lines common to two files. Both files must be sorted.
> More information: <https://www.gnu.org/software/coreutils/comm>.

- Produce three tab-separated columns: lines only in first file, lines only in second file and common lines:

`comm {{file1}} {{file2}}`

- Print only lines common to both files:

`comm -12 {{file1}} {{file2}}`

- Print only lines common to both files, reading one file from `stdin`:

`cat {{file1}} | comm -12 - {{file2}}`

- Get lines only found in first file, saving the result to a third file:

`comm -23 {{file1}} {{file2}} > {{file1_only}}`

- Print lines only found in second file, when the files aren't sorted:

`comm -13 <(sort {{file1}}) <(sort {{file2}})`

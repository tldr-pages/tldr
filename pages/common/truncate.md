# truncate

> Shrink or extend the size of a file to the specified size.
> More information: <https://www.gnu.org/software/coreutils/truncate>.

- Set a size of 10 GB to an existing file, or create a new file with the specified size:

`truncate --size {{10G}} {{filename}}`

- Extend the file size by 50 MiB, fill with holes (which reads as zero bytes):

`truncate --size +{{50M}} {{filename}}`

- Shrink the file by 2 GiB, by removing data from the end of file:

`truncate --size -{{2G}} {{filename}}`

- Empty the file's content:

`truncate --size 0 {{filename}}`

- Empty the file's content, but do not create the file if it does not exist:

`truncate --no-create --size 0 {{filename}}`

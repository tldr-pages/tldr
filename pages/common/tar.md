# tar

> Archiving utility.
> Often combined with a compression method, such as gzip or bzip.
> More information: <https://www.gnu.org/software/tar>.

- Create an archive from files:

`tar -cf {{target.tar}} {{file1 file2 file3}}`

- Create a gzipped archive:

`tar -czf {{target.tar.gz}} {{file1 file2 file3}}`

- Extract an archive in a target directory:

`tar -xf {{source.tar}} -C {{directory}}`

- Extract a gzipped archive in the current directory:

`tar -xzf {{source.tar.gz}}`

- Extract a bzipped archive in the current directory:

`tar -xjf {{source.tar.bz2}}`

- Create a compressed archive, using archive suffix to determine the compression program:

`tar -caf {{target.tar.xz}} {{file1 file2 file3}}`

- List the contents of a tar file:

`tar -tvf {{source.tar}}`

- Extract files matching a pattern:

`tar -xf {{source.tar}} --wildcards {{"*.html"}}`

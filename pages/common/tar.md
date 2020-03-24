# tar

> Archiving utility.
> Often combined with a compression method, such as gzip or bzip.
> More information: <https://www.gnu.org/software/tar>.

- Create an archive from files:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- Create a gzipped archive:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- Create a gzipped archive from a directory using relative paths:

`tar czf {{target.tar.gz}} -C {{path/to/directory}} .`

- Extract a (compressed) archive into the current directory:

`tar xf {{source.tar[.gz|.bz2|.xz]}}`

- Extract an archive into a target directory:

`tar xf {{source.tar}} -C {{directory}}`

- Create a compressed archive, using archive suffix to determine the compression program:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- List the contents of a tar file:

`tar tvf {{source.tar}}`

- Extract files matching a pattern:

`tar xf {{source.tar}} --wildcards {{"*.html"}}`

- Extract a specific file without preserving the folder structure:

`tar xf {{source.tar}} {{source.tar/path/to/extract}} --strip-components={{depth_to_strip}}`

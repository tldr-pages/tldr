# tar

> Archiving utility.
> Often combined with a compression method, such as gzip or bzip.
> More information: <https://www.gnu.org/software/tar>.

- [C]reate an archive from [f]iles:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- [C]reate a g[z]ipped archive from [f]iles:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- [C]reate a g[z]ipped archive from [f]iles in a directory using relative paths:

`tar czf {{target.tar.gz}} -C {{path/to/directory}} .`

- E[x]tract [f]iles from a (compressed) archive into the current directory:

`tar xf {{source.tar[.gz|.bz2|.xz]}}`

- E[x]tract [f]iles from an archive into a target directory:

`tar xf {{source.tar}} -C {{directory}}`

- [C]reate a compressed archive, [a]utomatically determining the compression program from archive suffix, from [f]iles:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- Lis[t] [v]erbose information about the contents of a tar [f]ile:

`tar tvf {{source.tar}}`

- E[x]tract [f]iles matching a pattern:

`tar xf {{source.tar}} --wildcards {{"*.html"}}`

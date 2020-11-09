# pax

> Archiving and copying utility.

- List the contents of an archive:

`pax -f {{archive.tar}}`

- List the contents of a gzipped archive:

`pax -zf {{archive.tar.gz}}`

- Create an archive from files:

`pax -wf {{target.tar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Create an archive from files, using output redirection:

`pax -w {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} > {{target.tar}}`

- Extract an archive into the current directory:

`pax -rf {{source.tar}}`

- Copy to a directory, while keeping the original metadata; `target/` must exist:

`pax -rw {{path/to/file1}} {{path/to/directory1}} {{path/to/directory2}} {{target/}}`

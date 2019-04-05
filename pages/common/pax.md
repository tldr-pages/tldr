# pax

> Archiving and copying utility.

- List the contents of an archive:

`pax -f {{archive.tar}}`

- List the contents of a gzipped archive:

`pax -zf {{archive.tar.gz}}`

- Create an archive from files:

`pax -wf {{target.tar}} {{file1 file2 file3}}`

- Create an archive from files, using output redirection:

`pax -w {{file1 file2 file3}} > {{target.tar}}`

- Extract an archive into the current directory:

`pax -rf {{source.tar}}`

- Copy to a directory, while keeping the original metadata; target/ must exist:

`pax -rw {{file1 directory1 directory2}} {{target/}}`

# yaa

> Create and manipulate YAA archives.
> More information: <https://www.manpagez.com/man/1/yaa/>.

- Create an archive from a directory:

`yaa archive -d {{path/to/directory}} -o {{path/to/output.yaa}}`

- Create an archive from a file:

`yaa archive -i {{path/to/file}} -o {{path/to/output.yaa}}`

- Extract an archive to the current directory:

`yaa extract -i {{path/to/archive.yaa}}`

- List the contents of an archive:

`yaa list -i {{path/to/archive.yaa}}`

- Create an archive with a specific compression algorithm:

`yaa archive -a {{algorithm}} -d {{path/to/directory}} -o {{path/to/output.yaa}}`

- Create an archive with an 8 MB block size:

`yaa archive -b {{8m}} -d {{path/to/directory}} -o {{path/to/output.yaa}}`

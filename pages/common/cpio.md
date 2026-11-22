# cpio

> Copy files in and out of archives.
> Supports the following archive formats: cpio's custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar.
> More information: <https://www.gnu.org/software/cpio/manual/cpio.html#Invoking-cpio>.

- Take a file name from `stdin` and add it onto an archive (copy-[o]ut) in cpio's binary forma:

`echo "{{path/to/file}}" | cpio {{[-o|--create]}} >{{archive.cpio}}`

- Copy all files and directories in a directory and add them onto an archive (copy-[o]ut), in verbose mode:

`find {{path/to/directory}} | cpio {{[-ov|--create --verbose]}} >{{archive.cpio}}`

- Pick all files from an archive (copy-[i]n), generating directories where needed, in verbose mode:

`cpio <{{archive.cpio}} {{[-idv|--extract --make-directories --verbose]}}`

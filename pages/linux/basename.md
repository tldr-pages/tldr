# basename

> The basename command is used to extract and display the filename portion from a given path.
> It essentially removes all directory components and displays only the base name of the file or directory.
> More information: <https://man7.org/linux/man-pages/man1/basename.1.html>.

- The basic syntax of the basename command is as follows:

`basename [OPTION] NAME`
   
- Basic usage:

`basename /path/to/file.txt`

- Remove a specific file extension:

`basename /path/to/file.txt .txt`

- Extract the base name from a string:

`basename "Some/Long/Path/To/Directory/"`

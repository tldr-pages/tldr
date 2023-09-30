# basename

> The basename command is used to extract and display the filename portion from a given path.
> It essentially removes all directory components and displays only the base name of the file or directory.

- The basic syntax of the basename command is as follows:

`basename [OPTION] NAME`
   
- Basic usage:

`basename /path/to/file.txt`

- Remove a specific file extension:

`basename /path/to/file.txt .txt`

- Extract the base name from a string:

`basename "Some/Long/Path/To/Directory/"`

> For more details and additional options, you can refer to the basename manual page by running man basename.

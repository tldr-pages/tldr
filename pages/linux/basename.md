# basename

> The basename command is used to extract and display the filename portion from a given path.
> It essentially removes all directory components and displays only the base name of the file or directory.

- The basic syntax of the basename command is as follows:

`basename [OPTION] NAME`

> Where:

    - OPTION (optional) specifies various options you can use with basename.
    - NAME is the file path or string from which you want to extract the base name.


- Basic usage:

`basename /path/to/file.txt`

> Output:
    - file.txt

- Removing a specific file extension:

`basename /path/to/file.txt .txt`

> Output:
    - file

- Extracting the base name from a string:

`basename "Some/Long/Path/To/Directory/"`

> Output:
    - Directory

- For more details and additional options, you can refer to the basename manual page by running man basename

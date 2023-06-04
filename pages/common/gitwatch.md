# gitwatch

> Automatically commit file or directory changes to a git repository
> More information: <https://github.com/gitwatch/gitwatch>.

- Automatically commit any changes made to a file or directory

`gitwatch {{path/to/file_or_directory}}`

- Automatically commit changes, and push these to git repository:

`gitwatch -r {{remote_name}} {{path/to/file_or_directory}}`

- Automatically commit changes, and push these to a specific branch of the git repository:

`gitwatch -r {{remote_name}} -b {{branch_name}} {{path/to/file_or_directory}}`

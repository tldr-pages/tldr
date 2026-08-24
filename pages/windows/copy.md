# copy

> Copy files from one location to another.
> In PowerShell, this command is an alias of `Copy-Item`. This documentation is based on the Command Prompt (`cmd`) version of `copy`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/copy>.

- Copy a file to another location:

`copy {{path\to\source_file}} {{path\to\target_file}}`

- Copy a file into another directory, keeping the filename:

`copy {{path\to\source_file}} {{path\to\target_directory}}`

- Copy multiple files to a directory:

`copy {{path\to\file1 path\to\file2 ...}} {{path\to\target_directory}}`

- Copy all files from one directory to another directory:

`copy {{path\to\source_directory\*}} {{path\to\target_directory}}`

- Copy files with a specific extension:

`copy {{path\to\source_directory\*.ext}} {{path\to\target_directory}}`

- Copy a file and prompt before overwriting:

`copy /-y {{path\to\source_file}} {{path\to\target_file}}`

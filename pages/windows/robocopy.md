# robocopy

> Robust File and Folder Copy.
> By default files will only be copied if the source and destination have different time stamps or different file sizes.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Copy all `.jpg` and `.bmp` files from one directory to another:

`robocopy {{path/to/source}} {{path/to/destination}} {{*.jpg}} {{*.bmp}}`

- Copy all files and subdirectories, including empty ones:

`robocopy {{path/to/source}} {{path/to/destination}} /E`

- Mirror/Sync a directory, deleting anything not in source and include all attributes and permissions:

`robocopy {{path/to/source}} {{path/to/destination}} /MIR /COPYALL`

- Copy all files and subdirectories, excluding source files that are older than destination files:

`robocopy {{path/to/source}} {{path/to/destination}} /E /XO`

- List all files 50 MB or larger instead of copying them:

`robocopy {{path/to/source}} {{path/to/destination}} /MIN:{{52428800}} /L`

- Allow resuming if network connection is lost and limit retries to 5 and wait time to 15 sec:

`robocopy {{path/to/source}} {{path/to/destination}} /Z /R:5 /W:15`

- Display detailed usage information:

`robocopy /?`

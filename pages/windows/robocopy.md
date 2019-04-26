# robocopy

> Robust File and Folder Copy. By default Robocopy will only copy a file if the source and destination have different time stamps or different file sizes.

- Copy all .jpg and .bmp files from one directory to another:

`robocopy {{path/to/directory}} {{path/to/destination}} *.jpg *.bmp`

- Copy all files and subdirectories, including empty ones:

`robocopy {{path/to/directory}} {{path/to/destination}} /E`

- Mirror a directory. Same as /E but also deletes anything not in source:

`robocopy {{path/to/directory}} {{path/to/destination}} /MIR`

- Copy all files and subdirectories, excluding older files:

`robocopy {{path/to/file_or_directory}} {{path/to/destination}} /E /XO`

- List all files 50 MBytes or larger in size:

`robocopy {{path/to/file_or_directory}} {{path/to/destination}} /MIN:52428800 /L`

- Allow resuming if network connection is lost:

`robocopy {{path/to/file_or_directory}} {{path/to/destination}} /Z`

- Display detailed usage information:

`robocopy /?`

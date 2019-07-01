# xcopy

> Copy files and directory trees.

- Copy the file(s) to the specified destination:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}}`

- List files that will be copied before copying:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /p`

- Copy the directory structure only, excluding files:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /t`

- Include empty directories when copying:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /e`

- Keep the source ACL in the destination:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /o`

- Allow resuming when network connection is lost:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /z`

- Disable the prompt when the file exists in the destination:

`xcopy {{path/to/file_or_directory}} {{path/to/destination}} /y`

- Display detailed usage information:

`xcopy /?`

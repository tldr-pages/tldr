# xcopy

> Copy files and directory trees.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Copy the file(s) to the specified destination:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}}`

- List files that will be copied before copying:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /p`

- Copy the directory structure only, excluding files:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /t`

- Include empty directories when copying:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /e`

- Keep the source ACL in the destination:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /o`

- Allow resuming when network connection is lost:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /z`

- Disable the prompt when the file exists in the destination:

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /y`

- Display help:

`xcopy /?`

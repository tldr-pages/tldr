# onefetch

> Display project information and code statistics for a local Git repository.
> More information: <https://github.com/o2sh/onefetch/wiki/command-line-options>.

- Display statistics for the Git repository in the current working directory:

`onefetch`

- Display statistics for the Git repository in the specified directory:

`onefetch {{path/to/directory}}`

- Ignore commits made by bots:

`onefetch --no-bots`

- Ignore merge commits:

`onefetch --no-merges`

- Don't print the ASCII art of the language logo:

`onefetch --no-art`

- Show `n` authors, languages, or file churns (default: 3, 6, and 3 respectively):

`onefetch --number-of-{{authors|languages|file-churns}} {{n}}`

- Ignore the specified files and directories:

`onefetch {{[-e|--exclude]}} {{path/to/file_or_directory|regular_expression}}`

- Only detect languages from the specified categories (default: programming and markup):

`onefetch {{[-T|--type]}} {{programming|markup|prose|data}}`

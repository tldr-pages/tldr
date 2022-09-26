# scalafmt

> Code formatter for Scala.
> Configurations are stored in the `.scalafmt.conf` file.
> More information: <https://scalameta.org/scalafmt>.

- Reformat all `.scala` files in the current directory recursively:

`scalafmt`

- Reformat specific files or directories with a custom formatting configuration:

`scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory}} {{path/to/file_or_directory}} {{...}}`

- Check if files are correctly formatted, returning `0` if all files respect the formatting style:

`scalafmt --config {{path/to/.scalafmt.conf}} --test`

- Exclude files or directories:

`scalafmt --exclude {{path/to/file_or_directory}} {{...}}`

- Format only files that were edited against the current Git branch:

`scalafmt --config {{path/to/.scalafmt.conf}} --mode diff`

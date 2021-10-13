# scalafmt

> Code formatter for Scala: Scalafmt is a formatter written in and for the Scala language. It is primarily designed to operate on entire text files.
> The formatting configuration is determined by searching for the `.scalafmt.conf` file.
> The configuration is searched firstly in the current directory, secondly, by searching in the root directory of the current git repo and finally, if  any configuration file is found, it proceeds with the default style.
> Rules for configuring the formatting: <https://scalameta.org/scalafmt/docs/configuration.html>.
> More information: <https://scalameta.org/scalafmt>.

- Reformat all the `.scala` files in the current directory recursively:

`scalafmt`

- Reformat specific files or directories with custom formatting configuration:

`scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory}} {{path/to/file_or_directory}} ...`

- Check if files are correctly formatted (return -1 if not):

`scalafmt --config {{path/to/.scalafmt.conf}} --test`

- Exclude files or directories:

`scalafmt --exclude myTargetDir myTargetFile.scala`

- Format only files that were edited against the current branch:

`scalafmt --config {{path/to/.scalafmt.conf}} --mode diff`

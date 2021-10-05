# scalafmt

> Code formatter for Scala: Scalafmt is a formatter written in and for the Scala language. It is primarily designed to operate on entire text files.
> Rules for configuring the formatting: <https://scalameta.org/scalafmt/docs/configuration.html>
> More information: <https://scalameta.org/scalafmt>.

- Standard formatting for all the `.scala` files in the current directory and recursively, it searches the configuration in the following order Format all files in the current project, the configuration is determined in this order:
  1.  `.scalafmt.conf` file in current directory
  2.  `.scalafmt.conf` inside the root directory of the current git repo
  3.  no configuration, default style

`scalafmt`

- Reformat specific files or directories with custom formatting configuration:

`scalafmt --config customConfigDir/.scalafmt.conf myFile1.scala myFile2.scala myDir`

- Check if files are correctly formatted (return -1 if not):

`scalafmt --config customDir/.scalafmt.conf --test`

- Format excluding files of directory:

`scalafmt --exclude myTargetDir myTargetFile.scala`

- Format only files that were edited against the master branch (files edited in the current commit allowing incremental refectory of a codebase):

`scalafmt --config customDir/.scalafmt.conf --mode diff`

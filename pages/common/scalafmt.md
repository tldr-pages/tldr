# scalafmt

> Code formatter for Scala: Scalafmt is a formatter written in and for the Scala language. It is primarily designed to operate on entire text files.
> Rules for configuring the formatting: <https://scalameta.org/scalafmt/docs/configuration.html>
> More information: <https://scalameta.org/scalafmt>.

- Standard formatting for all the `.scala` files available in the current directory (and recursively in all the children directories).
The formatting configuration is determined by searching for the `.scalafmt.conf` file.
The configuration is searched firstly in the current directory, secondly, by searching in the root directory of the current git repo and finally, if  any configuration file is found, it proceeds with the default style:

`scalafmt`

- Reformat specific files or directories with custom formatting configuration:

`scalafmt --config customConfigDir/.scalafmt.conf myFile1.scala myFile2.scala myDir`

- Check if files are correctly formatted (return -1 if not):

`scalafmt --config customDir/.scalafmt.conf --test`

- Format excluding files of directory:

`scalafmt --exclude myTargetDir myTargetFile.scala`

- Format only files that were edited against the master branch (files edited in the current commit allowing incremental refectory of a codebase):

`scalafmt --config customDir/.scalafmt.conf --mode diff`

# java_home

> Return a value for $JAVA_HOME or execute command using this variable.
> More information: <https://www.unix.com/man-page/osx/1/java_home>.

- List JVMs based on a specific version:

`java_home --version {{1.5+}}`

- List JVMs based on a specific [arch]itecture:

`java_home --arch {{i386}}`

- List JVMs based on a specific tasks (defaults to `CommandLine`):

`java_home --datamodel {{Applets|WebStart|BundledApp|JNI|CommandLine}}`

- List JVMs in a XML format:

`java_home --xml`

- Display help:

`java_home --help`

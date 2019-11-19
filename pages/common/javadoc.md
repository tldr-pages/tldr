# javadoc

> Generate Java API documentation in HTML format from source code.
> More information: <https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>.

- Generate documentation for Java source code and save the result in a directory:

`javadoc -d {{path/to/directory/}} {{path/to/java_source_code}}`

- Generate documentation with a specific encoding:

`javadoc -docencoding {{UTF-8}} {{path/to/java_source_code}}`

- Generate documentation excluding some packages:

`javadoc -exclude {{package_list}} {{path/to/java_source_code}}`

# javadoc

> Generate Java API documentation in HTML format from source code.
> More information: <https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>.

- Generate documentation for Java source code and save the result in the directory:

`javadoc -d {{path/to/directory/}} {{path/to/java_source_code}}`

- Generate documentation with specific encoding:

`javadoc -docencoding {{encoding_name}} {{java_source_code}}`

- Generate documentation exclude some packages:

`javadoc -exclude {{package_list}} {{java_source_code}}`

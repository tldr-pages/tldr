# javap

> Disassemble one or more class files and list them.
> More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/javap.html>.

- Disassemble and list a `.class` file:

`javap {{path/to/file.class}}`

- Disassemble and list multiple `.class` files:

`javap {{path/to/file1.class path/to/file2.class ...}}`

- Disassemble and list a built-in class file:

`javap java.{{package}}.{{class}}`

- Display help:

`javap -help`

- Display version:

`javap -version`

# astyle

> Source code indenter, formatter, and beautifier for the C, C++, C# and Java programming languages.
> A copy of the original file is created with an .orig appended to the original file name. 

- Apply default style, 4 spaces per indent and no formatting changes:

`astyle {source_file}`

- Apply java style, attached braces:

`astyle  --style=java {path/to/file}`

- Apply allman style, broken braces:

`astyle --style=allman {path/to/file}`

- Apply custom indent using spaces, between 2 and 20:

`astyle --indent=spaces={number_of_spaces} {path/to/file}`

- Apply custom indent using tabs, between 2 and 20:

`astyle --indent=tab={number_of_tabs} {path/to/file}`

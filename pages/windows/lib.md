# lib

> The Microsoft Library Manager for creating and managing static libraries of object files.
> More information: <https://learn.microsoft.com/cpp/build/reference/lib-reference>.

- Create a static library from object files:

`lib /OUT :{{path/to/library.lib}} {{path/to/file1.obj path/to/file2.obj ...}}`

- List the contents of a library:

`lib /LIST {{path/to/library.lib}}`

- Add an object file to an existing library:

`lib {{path/to/library.lib}} {{path/to/file.obj}}`

- Remove an object file from a library:

`lib /REMOVE :{{path/to/file.obj}} {{path/to/library.lib}}`

- Extract an object file from a library:

`lib /EXTRACT :{{path/to/file.obj}} {{path/to/library.lib}}`

- Create an import library from a DLL:

`lib /DEF :{{path/to/definition.def}} /OUT:{{path/to/import.lib}}`

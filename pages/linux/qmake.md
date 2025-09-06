# qmake

> Generate Makefiles from Qt project files.
> More information: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Generate a `Makefile` from a project file in the current directory:

`qmake`

- Specify `Makefile` and project file locations:

`qmake -o {{path/to/Makefile}} {{path/to/project_file.pro}}`

- Generate a default project file:

`qmake -project`

- Compile a project:

`qmake && make`

- Enable debug mode:

`qmake -d`

- Display help:

`qmake -help`

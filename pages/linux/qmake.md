# qmake

> Generate Makefiles from project files.
> More information: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Generate a `Makefile` from a project file in the current directory:

`qmake`

- Specify `Makefile` and project file locations:

`qmake -o {{path/to/Makefile}} {{path/to/project_file.pro}}`

- Generate a default project file:

`qmake -project`

- Enable debug mode:

`qmake -d`

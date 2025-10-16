# qmake

> Cross-platform build system generator for Qt applications.
> More information: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Generate a Makefile from a Qt project file:

`qmake {{project.pro}}`

- Generate a Makefile with a specific configuration:

`qmake {{project.pro}} -config {{debug|release}}`

- Generate a Makefile with custom variables:

`qmake {{project.pro}} "{{VARIABLE=value}}"`

- Generate a Makefile for a specific platform:

`qmake {{project.pro}} -spec {{platform_spec}}`

- Create a new Qt project file:

`qmake -project -o {{project.pro}}`

- Display qmake properties:

`qmake -query`

- Generate a Makefile in a specific output directory:

`qmake {{project.pro}} -o {{path/to/output/directory/}}`

- Generate a Makefile with additional Qt modules:

`qmake {{project.pro}} "{{QT+=network sql}}"`

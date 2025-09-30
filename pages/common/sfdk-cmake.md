# sfdk cmake

> Executes cmake build step.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.cmake.adoc>.

- Run cmake:

`sfdk cmake`

- Run cmake in specified project directory:

`sfdk cmake {{project}}`

- Run cmake with extra arguments:

`sfdk cmake -- {{arguments}}`

- Run cmake build in current directory:

`sfdk cmake --build .`

- Run cmake build in current directory with extra cmake arguments:

`sfdk cmake --build . {{cmake-arguments}}`

- Run cmake build in current directory with extra build tool arguments:

`sfdk cmake --build . -- {{build-tool-arguments}}`

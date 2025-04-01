# sfdk cmake

> Executes cmake build step.
> More information: <https://docs.sailfishos.org/Develop/Apps/Tutorials/Building_packages_-_advanced_techniques/#building-the-sample-application>.

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

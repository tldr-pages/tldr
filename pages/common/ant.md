# ant

> Apache Ant: build and manage Java-based projects.
> More information: <https://ant.apache.org/manual/index.html>.

- Build a project with default build file `build.xml`:

`ant`

- Build a project using build file other than `build.xml`:

`ant {{[-f|-buildfile]}} {{buildfile.xml}}`

- Print information on possible targets for this project:

`ant {{[-p|-projecthelp]}}`

- Print debugging information:

`ant {{[-d|-debug]}}`

- Execute all targets that do not depend on fail target(s):

`ant {{[-k|-keep-going]}}`

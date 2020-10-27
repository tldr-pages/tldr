# ant

> Apache Ant.
> Tool for building and managing Java-based projects.
> More information: <https://ant.apache.org>.

- Build a project with default build file `build.xml`:

`ant`

- Build a project using build file other than `build.xml`:

`ant -f {{buildfile.xml}}`

- Print information on possible targets for this project:

`ant -p`

- Print debugging information:

`ant -d`

- Execute all targets that do not depend on fail target(s):

`ant -k`

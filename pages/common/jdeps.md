# jdeps

> Java class dependency analyzer.
> More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>.

- Analyze the dependencies of a `.jar` or `.class` file:

`jdeps {{path/to/file.class}}`

- Print a summary of all dependencies of a specific `.jar` file:

`jdeps {{path/to/file.jar}} -summary`

- Print all class-level dependencies of a `.jar` file:

`jdeps {{path/to/file.jar}} -verbose`

- Output the results of the analysis in a DOT file into a specific directory:

`jdeps {{path/to/file.jar}} -dotoutput {{path/to/directory}}`

- Display help:

`jdeps --help`

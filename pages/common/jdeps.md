# jdeps

> Java Class Dependency Analyzer.
> More information: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/jdeps.html>.

- Analyze the dependencies of a `.jar` or `.class` file:

`jdeps {{path/to/filename.class}}`

- Print a summary of all dependencies:

`jdeps {{path/to/filename.jar}} -summary`

- Print all class-level dependencies:

`jdeps {{filename.jar}} -verbose`

- Output the results of the analysis in form of a DOT file:

`jdeps {{path/to/filename.jar}} -dotoutput {{output/path}}`

- Display help:

`jdeps --help`

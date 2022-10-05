# jdeps

> Java Class Dependency Analyzer.
> More information: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/jdeps.html>.

- Analyze the dependencies of a jar or class file:

`jdeps {{filename.class}}`

- Print a dependency summary:

`jdeps {{filename.jar}} -summary`

- Print all class-level dependencies:

`jdeps {{filename.jar}} -verbose`

- Output the results of the analysis in form of a DOT file:

`jdeps {{filename.jar}} -dotoutput {{output/path}}`

- Display usage information for the jdeps command:

`jdeps --help`

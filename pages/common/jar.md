# jar

> Java applications/libraries packager.
> More information: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Recursively archive all files in the current directory into a .jar file:

`jar cf {{file.jar}} *`

- Unzip .jar/.war file to the current directory:

`jar -xvf {{file.jar}}`

- List a .jar/.war file content:

`jar tf {{path/to/file.jar}}`

- List a .jar/.war file content with verbose output:

`jar tvf {{path/to/file.jar}}`

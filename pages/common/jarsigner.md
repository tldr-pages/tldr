# jarsigner

> Sign and verify Java archive (JAR) files.
> More information: <https://docs.oracle.com/javase/9/tools/jarsigner.htm>.

- Sign a JAR file:

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- Sign a JAR file with a specific algorithm:

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- Verify the signature of a JAR file:

`jarsigner -verify {{path/to/file.jar}}`

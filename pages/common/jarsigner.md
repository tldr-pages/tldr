# jarsigner

> Sign and verify Java archive (`.jar`) files.
> More information: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jarsigner.html>.

- Sign a `.jar` file:

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- Sign a `.jar` file with a specific algorithm:

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- Verify the signature of a `.jar` file:

`jarsigner -verify {{path/to/file.jar}}`

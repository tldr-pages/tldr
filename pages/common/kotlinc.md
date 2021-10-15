# kotlinc

> Kotlin compiler.
> More information: <https://kotlinlang.org/docs/command-line.html>.

- Start a REPL (interactive shell):

`kotlinc`

- Compile a Kotlin file:

`kotlinc {{path/to/file.kt}}`

- Compile several Kotlin files:

`kotlinc {{path/to/file1.kt path/to/file2.kt ...}}`

- Execute a specific Kotlin Script file:

`kotlinc -script {{path/to/file.kts}}`

- Compile a Kotlin file into a self contained jar file with the Kotlin runtime library included:

`kotlinc {{path/to/file.kt}} -include-runtime -d {{path/to/file.jar}}`

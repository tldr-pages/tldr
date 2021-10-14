# kotlinc

> Kotlin Language Compiler.
> More information: <https://kotlinlang.org/docs/command-line.html>.

- Call a Kotlin interactive shell (REPL):

`kotlinc`

- Compile a Kotlin file:

`kotlinc {{file.kt}}`

- Compile several Kotlin files:

`kotlinc {{file1.kt}} {{file2.kt}} {{file3.kt}}`

- Execute a given Kotlin Script file:

`kotlinc -script file.kts`

- Compile a Kotlin file into a self contained jar file with the Kotlin runtime library included:

`kotlinc {{file.kt}} -include-runtime -d {{output.jar}}`

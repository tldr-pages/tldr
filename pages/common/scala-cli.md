# scala-cli

> Interact with the Scala programming language.
> More information: <https://scala-cli.virtuslab.org/docs/overview/>.

- Start a REPL (interactive shell) using a specific Scala and JVM version:

`scala-cli --scala {{3.1.0}} --jvm {{temurin:17}}`

- Compile and run a Scala script:

`scala-cli run {{path/to/script.scala}}`

- Compile and test a Scala script:

`scala-cli test {{path/to/script.scala}}`

- Format a Scala script, updating the file in-place:

`scala-cli fmt {{path/to/script.scala}}`

- Generate files for IDE (VSCode and IntelliJ) support:

`scala-cli setup-ide {{path/to/script.scala}}`

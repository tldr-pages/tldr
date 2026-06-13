# sbt

> Build tool for Scala and Java projects.
> More information: <https://www.scala-sbt.org/1.x/docs/>.

- Start a REPL (interactive shell):

`sbt`

- Create a new Scala project from an existing Giter8 template hosted on GitHub:

`sbt new {{scala/hello-world.g8}}`

- Compile and run all tests:

`sbt test`

- Delete all generated files in the `target` directory:

`sbt clean`

- Compile the main sources in `src/main/scala` and `src/main/java` directories:

`sbt compile`

- Use the specified version of sbt:

`sbt -sbt-version {{version}}`

- Use a specific jar file as the sbt launcher:

`sbt -sbt-jar {{path}}`

- List all sbt options:

`sbt -h`

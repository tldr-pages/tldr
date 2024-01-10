# jbang

> Easily create, edit and run self-contained source-only Java programs.
> See also: `java`.
> More information: <https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- Initialize a simple Java class:

`jbang init {{path/to/file.java}}`

- Initialize a Java class (useful for scripting):

`jbang init --template={{cli}} {{path/to/file.java}}`

- Use `jshell` to explore and use a script and any dependencies in a REPL editor:

`jbang run --interactive`

- Setup a temporary project to edit a script in an IDE:

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{path/to/script.java}}`

- Run a Java code snippet (Java 9 and later):

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- Run command line application:

`jbang {{path/to/file.java}} {{command}} {{arg1 arg2 ...}}`

- Install a script on the user's `$PATH`:

`jbang app install --name {{command_name}} {{path/to/script.java}}`

- Install a specific version of JDK to be used with `jbang`:

`jbang jdk install {{version}}`

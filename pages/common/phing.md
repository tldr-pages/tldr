# phing

> A PHP build tool based on Apache Ant.
> More information: <https://www.phing.info>.

- Perform the default task in the `build.xml` file:

`phing`

- Initialize a new build file:

`phing -i {{path/to/build.xml}}`

- Perform a specific task:

`phing {{task_name}}`

- Use the given build file path:

`phing -f {{path/to/build.xml}} {{task_name}}`

- Log to the given file:

`phing -logfile {{path/to/log_file}} {{task_name}}`

- Use custom properties in the build:

`phing -D{{property}}={{value}} {{task_name}}`

- Specify a custom listener class:

`phing -listener {{class_name}} {{task_name}}`

- Build using verbose output:

`phing -verbose {{task_name}}`

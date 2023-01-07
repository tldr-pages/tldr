# serialver

> Returns the serialVersionUID of classes.
> It does not set a security manager by default.
> More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/serialver.html>.

- Display the serialVersionUID of a class:

`serialver {{classnames}}`

- Display the serialVersionUID for a colon-separated list of classes and resources:

`serialver -classpath {{path/to/directory}} {{classname1:classname2:...}}`

- Use a specific option from reference page of Java application launcher to the Java Virtual Machine:

`serialver -Joption {{classnames}}`

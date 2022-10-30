# serialver

> Returns the serialVersionUID of classes.
> It does not set a security manager by default.
> More information: <https://manned.org/serialver>.

- Display the serialVersionUID of a class:

`serialver {{classnames}}`

- Display the user interface, enter full class name and press show to view the serial version:

`serialver -show {{classnames}}`

- Display the serialVersionUID for a colon-separated list of classes and resources:

`serialver -classpath {{directory}} {{classname1:classname2:...}}`

- Pass specified option from reference page of Java application launcher to the Java Virtual Machine:

`serialver -Joption {{classnames}}`

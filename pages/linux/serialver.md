# serialver

> Returns the serialVersionUID of classes.
> It does not set a security manager by default.
> More information: <https://manned.org/serialver.1>.

- Displaying serialVersionUID of a class:

`serialver {{classnames}}`

- Displaying the user interface, enter full class name and press show to view the serial version:

`serialver -show {{classnames}}`

- Displaying serialVersionUID of a class in a specific package, separate classes and resources with a colon(:):

`serialver -classpath {{directory}} {{classnames}}`

- Passes specified option from reference page of Java application launcher to  the Java Virtual Machine:

`serialver -Joption {{classnames}}`

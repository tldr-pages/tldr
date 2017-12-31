# java

> Java Application Launcher.

- Execute a java .class file that contains a main method by using just the class name:

`java {{classname}}`

- Custom input and output files. Preferably .txt files. This is useful when you don’t want to input from keyboard every time you run your class. Outputs from `System.out.println();` are saved in the output file:

`java {{classname}} <{{path/to/inputfile}}> {{path/to/outputfile}}`

- Execute a .jar program:

`java -jar {{filename.jar}}`

- Display JDK, JRE and HotSpot versions:

`java -version`

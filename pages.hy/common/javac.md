# javac

> Java հավելվածի կոմպիլյատոր:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html>:.

- Կազմել `.java` ֆայլ՝:

`javac {{path/to/file.java}}`

- Կազմել մի քանի `.java` ֆայլ՝:

`javac {{path/to/file1.java path/to/file2.java ...}}`

- Կազմել բոլոր `.java` ֆայլերը ընթացիկ գրացուցակում.:

`javac {{*.java}}`

- Կազմեք `.java` ֆայլը և ստացված դասի ֆայլը տեղադրեք որոշակի գրացուցակում.:

`javac -d {{path/to/directory}} {{path/to/file.java}}`

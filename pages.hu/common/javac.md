# javac

> Java alkalmazásfordító. További információ: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/javac.html>.

- Fordítson le egy `.java` fájlt:

`javac {{file.java}}`

- Több `.java` fájl fordítása:

`javac {{file1.java}} {{file2.java}} {{file3.java}}`

- Az aktuális könyvtárban található összes `.java` fájl lefordítása:

`javac {{*.java}}`

- Egy `.java` fájl lefordítása és az így kapott osztályfájl elhelyezése egy adott könyvtárban:

`javac -d {{path/to/directory}} {{file.java}}`

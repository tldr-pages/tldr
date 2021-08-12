# javadoc

> Generați documentația API Java în format HTML din codul sursă.
> Mai multe informaţii: <https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>

- Generați documentația pentru codul sursă Java și salvați rezultatul într-un director:

`javadoc -d {{path/to/directory/}} {{path/to/java_source_code}}`

- Generați documentația cu o codificare specifică:

`javadoc -docencoding {{UTF-8}} {{path/to/java_source_code}}`

- Generarea documentației excluzând unele pachete:

`javadoc -exclude {{package_list}} {{path/to/java_source_code}}`

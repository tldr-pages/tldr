# java

> Средство запуска Java-приложений.
> Больше информации: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>.

- Выполнить файл Java `.class`, содержащий метод main, используя только имя класса:

`java {{имя_класса}}`

- Выполнить Java-программу с использованием дополнительных сторонних или пользовательских классов:

`java -classpath {{путь/к/классам1}}:{{путь/к/классам2}}:. {{имя_класса}}`

- Выполнить `.jar`-программу:

`java -jar {{имя_файла.jar}}`

- Выполнить `.jar`-программу с отладкой, ожидающей подключения на порту 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{имя_файла.jar}}`

- Показать справку:

`java -help`

- Показать версии JDK, JRE и HotSpot:

`java -version`

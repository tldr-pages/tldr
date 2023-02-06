# java_home

> A $JAVA_HOME értékének visszaadása vagy parancs végrehajtása a változó használatával. További információ: <https://www.unix.com/man-page/osx/1/java_home>.

- JVM-ek listázása egy adott verzió alapján:

`java_home --version {{1.5+}}`

- JVM-ek listázása egy adott \[arch\]itektúra alapján:

`java_home --arch {{i386}}`

- List JVMs based on a specific tasks (defaults to `CommandLine`):

`java_home --datamodel {{Applets|WebStart|BundledApp|JNI|CommandLine}}`

- JVM-ek listázása XML formátumban:

`java_home --xml`

- Súgó megjelenítése:

`java_home --help`

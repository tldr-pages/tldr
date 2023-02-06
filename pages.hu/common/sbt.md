# sbt

> Építőeszköz Scala és Java projektekhez. További információ: <https://www.scala-sbt.org/1.x/docs/>.

- Indítson el egy REPL-t (interaktív shell):

`sbt`

- Hozzon létre egy új Scala projektet egy meglévő, a GitHubon tárolt Giter8 sablonból:

`sbt new {{scala/hello-world.g8}}`

- Fordítsa le és futtassa az összes tesztet:

`sbt test`

- Törölje az összes generált fájlt a `target` könyvtárban:

`sbt clean`

- Fordítsa le a fő forrásokat a `src/main/scala` és `src/main/java` könyvtárakban:

`sbt compile`

- Használja az sbt megadott verzióját:

`sbt -sbt-version {{version}}`

- Egy adott jar fájl használata sbt indítóprogramként:

`sbt -sbt-jar {{path}}`

- Az összes sbt opció felsorolása:

`sbt -h`

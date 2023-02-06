# ant

> Apache Ant. Eszköz Java-alapú projektek építéséhez és kezeléséhez. További információ: <https://ant.apache.org>.

- Projekt építése az alapértelmezett építési fájlokkal `build.xml`:

`ant`

- Projekt építése a `build.xml`-től eltérő buildfájl használatával:

`ant -f {{buildfile.xml}}`

- Információ nyomtatása a projekt lehetséges célpontjairól:

`ant -p`

- Hibakeresési információk nyomtatása:

`ant -d`

- Az összes olyan célpont végrehajtása, amely nem függ a hibás célpont(ok)tól:

`ant -k`

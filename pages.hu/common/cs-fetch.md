# cs fetch

> A Fetch egy vagy több függőség JAR-ját hívja le. További információ: <https://get-coursier.io/docs/cli-fetch>.

- Egy jar egy adott verziójának lehívása:

`cs fetch {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Egy csomag lekérése és a kiválasztott csomagnak megfelelő classpath kiértékelése egy env var-ban:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- Egy adott jar forrásának lekérdezése:

`cs fetch --sources {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- A javadoc jar-ek lekérdezése:

`cs fetch --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Függőség lekérdezése a javadoc jar-okkal és a forrás jar-okkal:

`cs fetch --default={{true}} --sources --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Függőségi fájlokból származó jar-ek lekérése:

`cs fetch {{--dependency-file path/to/file1 --dependency-file path/to/file2 ...}}`

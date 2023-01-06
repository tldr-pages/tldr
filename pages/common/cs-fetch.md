# cs fetch

> Fetch fetches the JARs of one or more dependencies.
> More information: <https://get-coursier.io/docs/cli-fetch>.

- Fetch a specific version of a jar:

`cs fetch {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Fetch a package and evaluate the classpath corresponding to the selected package in an env var:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- Fetch the source jar:

`cs fetch --sources {{groupId}}:{{artifactId}}:{{artifactVersion}}`

- Fetch the javadoc jars:

`cs fetch --javadoc {{groupId}}:{{artifactId}}:{{artifactVersion}}`

- Fetch dependency with javadoc jars and source jars:

`cs fetch --default=true --sources --javadoc {{groupId}}:{{artifactId}}:{{artifactVersion}}`

- Fetch jars coming from dependency files:

`cs fetch --dependency-file file_1 --dependency-file file_2`

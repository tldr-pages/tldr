# cs բեռնում

> Fetch-ը վերցնում է կախվածությունների JAR-ները:.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-fetch>:.

- Վերցրեք `.jar`-ի որոշակի տարբերակ.:

`cs fetch {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Վերցրեք փաթեթ և գնահատեք ընտրված փաթեթին համապատասխան դասընթացը env var-ում.:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- Ստացեք որոշակի `.jar` աղբյուր.:

`cs fetch --sources {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Վերցրեք javadoc բանկաները.:

`cs fetch --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Ստացեք կախվածությունը javadoc բանկաների և աղբյուրի բանկաների միջոցով.:

`cs fetch --default={{true}} --sources --javadoc {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Վերցրեք բանկաները, որոնք գալիս են կախվածության ֆայլերից.:

`cs fetch {{--dependency-file path/to/file1 --dependency-file path/to/file2 ...}}`

# cs fetch

> Fetch는 종속성의 JAR를 가져옴.
> 더 많은 정보: <https://get-coursier.io/docs/cli-fetch>.

- jar의 특정 버전을 가져옴:

`cs fetch {{그룹_아이디}}:{{아티팩트_아이디}}:{{아티팩트_버전}}`

- 패키지를 가져오고 env var에서 선택한 패키지에 해당하는 클래스 경로를 평가:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- 특정 jar의 소스를 가져옴:

`cs fetch --sources {{그룹_아이디}}:{{아티팩트_아이디}}:{{아티팩트_버전}}`

- javadoc jar를 가져옴:

`cs fetch --javadoc {{그룹_아이디}}:{{아티팩트_아이디}}:{{아티팩트_버전}}`

- javadoc jar 및 소스 jar로 종속성을 가져옴:

`cs fetch --default={{true}} --sources --javadoc {{그룹_아이디}}:{{아티팩트_아이디}}:{{아티팩트_버전}}`

- 종속성 파일에서 오는 jar 가져오기:

`cs fetch {{--dependency-file 경로/대상/파일1 --dependency-file 경로/대상/파일2 ...}}`

# scalafmt

> Scala 코드를 위한 코드 포매터.
> 설정은 `.scalafmt.conf` 파일에 저장됩니다.
> 더 많은 정보: <https://scalameta.org/scalafmt>.

- 현재 디렉토리의 모든 `.scala` 파일을 재귀적으로 재포맷:

`scalafmt`

- 특정 파일 또는 디렉토리를 사용자 정의 포맷 설정으로 재포맷:

`scalafmt --config {{경로/대상/.scalafmt.conf}} {{경로/대상/파일_또는_디렉토리}} {{경로/대상/파일_또는_디렉토리}} {{...}}`

- 파일이 올바르게 포맷되었는지 확인하고, 모든 파일이 포맷 스타일을 준수하면 `0` 반환:

`scalafmt --config {{경로/대상/.scalafmt.conf}} --test`

- 파일이나 디렉토리 제외:

`scalafmt --exclude {{경로/대상/파일_또는_디렉토리}} {{...}}`

- 현재 Git 브랜치에 대해 수정된 파일만 포맷:

`scalafmt --config {{경로/대상/.scalafmt.conf}} --mode diff`

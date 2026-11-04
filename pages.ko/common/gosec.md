# gosec

> Go 소스 코드의 보안 취약점 검사.
> 참고: `./...`는 Go 도구에서 사용하는 패키지 패턴. 현재 패키지와 현재 디렉터리 아래의 모든 하위 패키지를 재귀적으로 의미.
> 더 많은 정보: <https://github.com/securego/gosec>.

- 현재 디렉터리의 Go 패키지를 재귀적으로 검사:

`gosec ./...`

- 지정한 Go 패키지 검사:

`gosec {{경로/대상/패키지}}`

- Go 패키지를 재귀적으로 검사하고 결과를 파일로 저장:

`gosec -fmt {{json|yaml|csv|html|sonarqube|golint|sarif|junit-xml}} -out {{경로/대상/리포트}} {{./...}}`

- 지정한 규칙만 사용하여 검사 (기본값: 모든 규칙):

`gosec -include {{G101,G203,G401,...}} {{./...}}`

- 지정한 디렉터리를 검사 대상에서 제외:

`gosec -exclude-dir {{경로/대상/제외될_디렉터리}} {{./...}}`

- 지정한 심각도(severity)와 신뢰도(confidence) 수준으로 검사 level:

`gosec -severity {{low|medium|high}} -confidence {{low|medium|high}} {{./...}}`

- 지정한 규칙을 검사 대상에서 제외:

`gosec -exclude {{G101,G304,G401,...}} {{./...}}`

- 테스트 파일도 함께 검사:

`gosec -tests {{./...}}`

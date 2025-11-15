# snyk

> 코드의 취약점을 찾아 위험을 해결합니다.
> 더 많은 정보: <https://docs.snyk.io/snyk-cli/commands>.

- Snyk 계정에 로그인:

`snyk auth`

- 코드에서 알려진 취약점을 테스트:

`snyk test`

- 로컬 Docker 이미지에서 알려진 취약점을 테스트:

`snyk test --docker {{docker_이미지}}`

- 종속성과 취약점 상태를 snyk.io에 기록:

`snyk monitor`

- 취약점을 자동으로 패치하고 무시:

`snyk wizard`

# subfinder

> 웹사이트의 유효한 하위 도메인을 발견.
> 버그 바운티에 유용하고 침투 테스트에 안전하도록 설계된 패시브 프레임워크.
> 더 많은 정보: <https://docs.projectdiscovery.io/opensource/subfinder/usage>.

- 특정 [d] 도메인의 하위 도메인 찾기:

`subfinder -d {{example.com}}`

- 발견된 하위 도메인만 표시:

`subfinder -silent -d {{example.com}}`

- 활성 하위 도메인만 표시:

`subfinder -nW -d {{example.com}}`

- 모든 소스를 사용하여 열거:

`subfinder -all -d {{example.com}}`

- 쉼표로 구분된 [r] 리졸버 목록 사용:

`subfinder -r {{8.8.8.8,1.1.1.1,...}} -d {{example.com}}`

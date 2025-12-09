# sherlock

> 소셜 네트워크에서 사용자명을 찾습니다.
> 더 많은 정보: <https://github.com/sherlock-project/sherlock>.

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 [f]파일에 저장:

`sherlock {{사용자명}} --output {{경로/대상/파일}}`

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 [f]폴더에 저장:

`sherlock {{사용자명1 사용자명2 ...}} --folderoutput {{경로/대상/폴더}}`

- Tor 네트워크를 사용하여 소셜 네트워크에서 특정 사용자명 검색:

`sherlock --tor {{사용자명}}`

- 각 요청 후 새로운 Tor 회로로 요청 수행:

`sherlock --unique-tor {{사용자명}}`

- 프록시를 사용하여 소셜 네트워크에서 특정 사용자명 검색:

`sherlock {{사용자명}} --proxy {{프록시_URL}}`

- 소셜 네트워크에서 특정 사용자명을 검색하고 결과를 기본 웹 브라우저에서 열기:

`sherlock {{사용자명}} --browse`

- 도움말 표시:

`sherlock --help`

# whatis

> 매뉴얼 페이지에서 한 줄 설명을 표시합니다.
> 더 많은 정보: <https://manned.org/whatis>.

- 매뉴얼 페이지에서 설명을 표시:

`whatis {{명령어}}`

- 설명을 줄 끝에서 잘리지 않게 표시:

`whatis --long {{명령어}}`

- 와일드카드와 일치하는 모든 명령어에 대한 설명 표시:

`whatis --wildcard {{net*}}`

- 정규 표현식을 사용하여 매뉴얼 페이지 설명 검색:

`whatis --regex '{{wish[0-9]\.[0-9]}}'`

- 특정 언어로 설명 표시:

`whatis --locale={{en}} {{명령어}}`

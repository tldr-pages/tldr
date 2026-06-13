# brew leaves

> 다른 설치된 formula나 cask의 의존성이 아닌 설치된 formula 목록을 표시.
> 더 많은 정보: <https://docs.brew.sh/Manpage#leaves---installed-on-request---installed-as-dependency>.

- 다른 설치된 formula 또는 cask에 의존하지 않는 설치된 formula 목록을 표시:

`brew leaves`

- 사용자가 직접 설치한 leaves만 표시:

`brew leaves {{[-r|--installed-on-request]}}`

- 의존성으로 설치된 leaves만 표시:

`brew leaves {{[-p|--installed-as-dependency]}}`

- 도움말 표시:

`brew leaves {{[-h|--help]}}`

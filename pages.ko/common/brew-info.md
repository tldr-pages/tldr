# brew info

> Homebrew 설치 정보와 formula에 대한 정보를 표시.
> 더 많은 정보: <https://docs.brew.sh/Manpage#info-abv-options-formulacask->.

- Homebrew 설치 통계를 표시:

`brew info`

- formula 또는 cask에 대한 추가 정보를 표시:

`brew info {{formula|cask}}`

- formula 또는 cask에 대한 자세한 정보를 표시:

`brew info {{[-v|--verbose]}} {{formula|cask}}`

- formula 또는 cask 정보를 JSON 형식으로 표시:

`brew info --json {{formula|cask}}`

- 현재 설치된 formula 목록을 JSON 형식으로 출력:

`brew info --json --installed`

- 도움말 표시:

`brew info {{[-h|--help]}}`

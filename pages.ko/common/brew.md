# brew

> macOS와 Linux를 위한 패키지 관리자.
> 더 많은 정보: <https://docs.brew.sh/Manpage>.

- 공식(formula) 혹은 캐스크(cask)의 최신 안정 버전을 설치 (개발 버전을 원한다면 `--devel` 사용):

`brew install {{formula}}`

- 설치된 모든 공식(formulae)과 캐스크(casks) 나열:

`brew list`

- 설치된 특정 공식(formula) 혹은 캐스크(cask) 업그레이드 (옵션이 주어지지 않으면 모든 공식과 캐스크 업그레이드):

`brew upgrade {{formula}}`

- Homebrew 저장소에서 Homebrew와 함께 모든 공식(formulae)과 캐스크(casks)의 최신 버전 가져오기:

`brew update`

- 최신 버전이 아닌 공식(formulae)과 캐스크(casks) 나열:

`brew outdated`

- 사용 가능한 공식(formulae)과 캐스크(casks) 검색:

`brew search {{text}}`

- 공식(formula) 혹은 캐스크(cask)에 대한 정보 표시 (버전, 설치 경로, 의존성 등):

`brew info {{formula}}`

- 설치된 Homebrew에 문제가 있는 확인:

`brew doctor`

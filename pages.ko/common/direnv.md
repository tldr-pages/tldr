# direnv

> 현재 디렉터리에 따라 환경 변수를 로드 및 언로드하는 쉘 확장.
> 더 많은 정보: <https://github.com/direnv/direnv>.

- 현재 디렉터리에 있는 `.envrc`를 로드하려면 direnv 권한을 부여:

`direnv allow {{.}}`

- 현재 디렉터리에 있는`.envrc`를 로드하기 위한 인증을 취소:

`direnv deny {{.}}`

- 기본 텍스트 편집기에서 `.envrc` 파일을 편집하고 종료 시 환경을 다시 로드:

`direnv edit {{.}}`

- 환경 다시 로드를 트리거:

`direnv reload`

- 일부 디버그 상태 정보를 출력:

`direnv status`

# dnf4

> RHEL 8/9 및 구버전 Fedora(pre-41)를 위한 패키지 관리자.
> 다른 패키지 관리자에서 같은 명령어는, <https://wiki.archlinux.org/title/Pacman/Rosetta>을 참고.
> 더 많은 정보: <https://dnf.readthedocs.io/en/latest/command_ref.html>.

- 설치된 패키지를 최신 사용 가능 버전으로 업그레이드:

`sudo dnf4 {{[up|upgrade]}}`

- 키워드로 패키지 검색:

`dnf4 {{[se|search]}} {{키워드1 키워드2 ...}}`

- 패키지 상세 정보 표시:

`dnf4 {{[if|info]}} {{패키지}}`

- 새로운 패키지 설치 (`--assumeyes` 사용 시 모든 프롬프트 자동 승인):

`sudo dnf4 {{[in|install]}} {{패키지1 패키지2 ...}}`

- 패키지 제거:

`sudo dnf4 {{[rm|remove]}} {{패키지1 패키지2 ...}}`

- 설치된 패키지 목록 표시:

`dnf4 {{[ls|list]}} --installed`

- 특정 명령을 제공하는 패키지 검색:

`dnf4 {{[wp|provides]}} {{명령어}}`

- 모든 과거 작업 기록 표시:

`dnf4 {{[hist|history]}}`

# apt

> Debian 기반 배포판을 위한 패키지 관리 도구.
> Ubuntu 16.04 이후 버전에서 대화형 사용 시 `apt-get`의 권장 대체 도구.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://manned.org/apt.8>.

- 사용 가능한 패키지 및 버전 목록 업데이트 (다른 `apt` 명령어 실행 전 권장):

`sudo apt update`

- 주어진 패키지 검색:

`apt search {{패키지}}`

- 패키지 정보 표시:

`apt show {{패키지}}`

- 패키지 설치 또는 최신 버전으로 업데이트:

`sudo apt install {{패키지}}`

- 패키지 제거 (`purge`를 사용하면 설정 파일도 함께 제거):

`sudo apt remove {{패키지}}`

- 모든 설치된 패키지를 최신 버전으로 업그레이드:

`sudo apt upgrade`

- 모든 패키지 나열:

`apt list`

- 설치된 패키지 나열:

`apt list {{[-i|--installed]}}`

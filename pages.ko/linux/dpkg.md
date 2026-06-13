# dpkg

> Debian 패키지 관리자.
> `deb`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://manned.org/dpkg>.

- 패키지 설치:

`sudo dpkg {{[-i|--install]}} {{경로/대상/파일.deb}}`

- 패키지 제거:

`sudo dpkg {{[-r|--remove]}} {{패키지}}`

- 설치된 패키지 나열:

`dpkg {{[-l|--list]}} {{패턴}}`

- 패키지의 내용 나열:

`dpkg {{[-L|--listfiles]}} {{패키지}}`

- 로컬 패키지 파일의 내용 나열:

`dpkg {{[-c|--contents]}} {{경로/대상/파일.deb}}`

- 특정 파일이 어떤 패키지에 속해 있는지 확인:

`dpkg {{[-S|--search]}} {{경로/대상/파일}}`

- 설치되었거나 이미 제거된 패키지 및 구성 파일 삭제:

`sudo dpkg {{[-P|--purge]}} {{패키지}}`

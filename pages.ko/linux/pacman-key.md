# pacman-key

> GnuPG를 사용하여 pacman의 키링을 관리하는 래퍼 스크립트.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://manned.org/pacman-key>.

- `pacman` 키링 초기화:

`sudo pacman-key --init`

- 기본 Arch Linux 키 추가:

`sudo pacman-key --populate`

- 공개 키링에서 키 나열:

`pacman-key {{[-l|--list-keys]}}`

- 지정된 키 추가:

`sudo pacman-key {{[-a|--add]}} {{경로/대상/키파일.gpg}}`

- 키 서버에서 키 수신:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|name|email}}"`

- 특정 키의 지문 출력:

`pacman-key {{[-f|--finger]}} "{{uid|name|email}}"`

- 가져온 키를 로컬에서 서명:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- 특정 키 제거:

`sudo pacman-key {{[-d|--delete]}} "{{uid|name|email}}"`

# pacman-key

> GnuPG를 사용하여 pacman의 키링을 관리하는 래퍼 스크립트.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman-key>.

- `pacman` 키링 초기화:

`sudo pacman-key --init`

- 기본 Arch Linux 키 추가:

`sudo pacman-key --populate {{archlinux}}`

- 공개 키링에서 키 나열:

`pacman-key --list-keys`

- 지정된 키 추가:

`sudo pacman-key --add {{경로/대상/키파일.gpg}}`

- 키 서버에서 키 수신:

`sudo pacman-key --recv-keys "{{uid|name|email}}"`

- 특정 키의 지문 출력:

`pacman-key --finger "{{uid|name|email}}"`

- 가져온 키를 로컬에서 서명:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- 특정 키 제거:

`sudo pacman-key --delete "{{uid|name|email}}"`

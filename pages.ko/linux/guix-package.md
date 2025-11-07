# guix package

> Guix 패키지를 설치, 업그레이드, 제거하거나 이전 구성으로 롤백합니다.
> 더 많은 정보: <https://guix.gnu.org/manual/en/guix.html#Invoking-guix-package>.

- 새 패키지 설치:

`guix package -i {{패키지}}`

- 패키지 제거:

`guix package -r {{패키지}}`

- 정규 표현식으로 패키지 데이터베이스 검색:

`guix package -s "{{검색_패턴}}"`

- 설치된 패키지 나열:

`guix package -I`

- 생성 목록 나열:

`guix package -l`

- 이전 생성으로 롤백:

`guix package --roll-back`

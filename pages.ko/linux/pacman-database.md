# pacman --database

> Arch Linux 패키지 데이터베이스를 조작합니다.
> 설치된 패키지의 특정 속성을 수정합니다.
> 관련 항목: `pacman`.
> 더 많은 정보: <https://manned.org/pacman.8>.

- 패키지를 암묵적으로 설치된 것으로 표시:

`sudo pacman -D --asdeps {{패키지}}`

- 패키지를 명시적으로 설치된 것으로 표시:

`sudo pacman -D --asexplicit {{패키지}}`

- 모든 패키지 의존성이 설치되었는지 확인:

`pacman -Dk`

- 모든 지정된 의존성이 사용 가능한지 확인하기 위해 저장소 검사:

`pacman -Dkk`

- 오류 메시지만 표시:

`pacman -Dkq`

- 도움말 표시:

`pacman -Dh`

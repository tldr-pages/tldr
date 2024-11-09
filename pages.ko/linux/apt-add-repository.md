# apt-add-repository

> `apt` 저장소 정의를 관리합니다.
> 더 많은 정보: <https://manned.org/apt-add-repository.1>.

- 새 `apt` 저장소 추가:

`apt-add-repository {{저장소_명세}}`

- `apt` 저장소 제거:

`apt-add-repository --remove {{저장소_명세}}`

- 저장소 추가 후 패키지 캐시 업데이트:

`apt-add-repository --update {{저장소_명세}}`

- 소스 패키지 활성화:

`apt-add-repository --enable-source {{저장소_명세}}`

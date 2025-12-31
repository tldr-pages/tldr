# add-apt-repository

> `apt` 저장소 정의를 관리합니다.
> 더 많은 정보: <https://manned.org/add-apt-repository>.

- 새 `apt` 저장소 추가:

`add-apt-repository {{저장소_명세}}`

- `apt` 저장소 제거:

`add-apt-repository {{[-r|--remove]}} {{저장소_명세}}`

- 저장소 추가 후 패키지 캐시 업데이트:

`add-apt-repository --update {{저장소_명세}}`

- 저장소에서 소스 패키지 다운로드 허용:

`add-apt-repository {{[-s|--enable-source]}} {{저장소_명세}}`

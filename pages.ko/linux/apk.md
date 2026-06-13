# apk

> Alpine Linux 패키지 관리 도구.
> 더 많은 정보: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- 모든 원격 저장소에서 저장소 색인 업데이트:

`apk update`

- 새 패키지 설치:

`apk add {{패키지}}`

- 패키지 제거:

`apk del {{패키지}}`

- 패키지를 복구하거나 주요 의존성을 수정하지 않고 업그레이드:

`apk fix {{패키지}}`

- 키워드를 통해 패키지 검색:

`apk search {{키워드}}`

- 특정 패키지에 대한 정보 표시:

`apk info {{패키지}}`

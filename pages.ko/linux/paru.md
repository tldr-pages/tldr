# paru

> AUR 헬퍼 및 pacman 래퍼.
> 더 많은 정보: <https://github.com/Morganamilo/paru>.

- 패키지를 대화식으로 검색하고 설치:

`paru {{패키지_이름_또는_검색어}}`

- 모든 패키지를 동기화하고 업데이트:

`paru`

- AUR 패키지 업그레이드:

`paru -Sua`

- 패키지 정보 확인:

`paru -Si {{패키지}}`

- `PKGBUILD` 및 기타 패키지 소스 파일을 AUR 또는 ABS에서 다운로드:

`paru --getpkgbuild {{패키지}}`

- 패키지의 `PKGBUILD` 파일 표시:

`paru --getpkgbuild --print {{패키지}}`

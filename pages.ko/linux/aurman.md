# aurman

> Arch User Repository에서 패키지를 빌드하고 설치하는 Arch Linux 유틸리티.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://github.com/polygamma/aurman#syntax>.

- 모든 패키지를 동기화하고 업데이트:

`aurman --sync --refresh --sysupgrade`

- `PKGBUILD` 파일의 변경 사항을 표시하지 않고 모든 패키지를 동기화하고 업데이트:

`aurman --sync --refresh --sysupgrade --noedit`

- 새 패키지 설치:

`aurman --sync {{패키지}}`

- `PKGBUILD` 파일의 변경 사항을 표시하지 않고 새 패키지 설치:

`aurman --sync --noedit {{패키지}}`

- 묻지 않고 새 패키지 설치:

`aurman --sync --noedit --noconfirm {{패키지}}`

- 공식 저장소와 AUR에서 키워드를 검색하여 패키지 검색:

`aurman --sync --search {{키워드}}`

- 특정 패키지 및 의존성 제거:

`aurman --remove --recursive --nosave {{패키지}}`

- 패키지 캐시 지우기 (모든 패키지를 삭제하려면 두 개의 `--clean` 플래그 사용):

`aurman --sync --clean`

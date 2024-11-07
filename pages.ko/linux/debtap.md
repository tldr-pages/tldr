# debtap

> Debian 패키지를 Arch Linux 패키지로 변환합니다.
> 같이 보기: `pacman-upgrade`.
> 더 많은 정보: <https://github.com/helixarch/debtap>.

- debtap 데이터베이스 업데이트 (최초 실행 전):

`sudo debtap --update`

- 지정된 패키지 변환:

`debtap {{경로/대상/패키지.deb}}`

- 메타데이터 파일 편집을 제외한 모든 질문을 건너뛰고 지정된 패키지 변환:

`debtap --quiet {{경로/대상/패키지.deb}}`

- PKGBUILD 파일 생성:

`debtap --pkgbuild {{경로/대상/패키지.deb}}`

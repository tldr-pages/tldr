# pkg_add

> OpenBSD에 패키지를 설치/업데이트합니다.
> 같이 보기: `pkg_info`, `pkg_delete`.
> 더 많은 정보: <https://man.openbsd.org/pkg_add>.

- 종속성을 포함하여 모든 패키지를 업데이트:

`pkg_add -u`

- 새로운 패키지 설치:

`pkg_add {{패키지}}`

- `pkg_info`의 원시 출력에서 패키지 설치:

`pkg_add -l {{경로/대상/파일}}`

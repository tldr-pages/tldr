# pkg_info

> OpenBSD의 패키지에 대한 정보를 확인합니다.
> 같이 보기: `pkg_add`, `pkg_delete`.
> 더 많은 정보: <https://man.openbsd.org/pkg_info>.

- 패키지 이름을 사용해 패키지 검색:

`pkg_info -Q {{패키지}}`

- `pkg_add -l`과 함께 사용할 설치된 패키지 목록을 출력:

`pkg_info -mz`

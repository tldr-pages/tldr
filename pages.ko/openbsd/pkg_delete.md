# pkg_delete

> OpenBSD에서 패키지를 제거합니다.
> 같이 보기: `pkg_add`, `pkg_info`.
> 더 많은 정보: <https://man.openbsd.org/pkg_delete>.

- 패키지 삭제:

`pkg_delete {{패키지}}`

- 사용되지 않는 의존성을 포함하여 패키지 삭제:

`pkg_delete -a {{패키지}}`

- 패키지의 Dry-run 삭제:

`pkg_delete -n {{패키지}}`

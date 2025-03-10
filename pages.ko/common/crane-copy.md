# crane copy

> 다이제스트 값을 유지하면서 소스에서 대상으로 원격 이미지를 효율적으로 복사.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- 소스에서 대상으로 이미지를 복사:

`crane copy {{소스}} {{대상}}`

- 모든 태그 복사:

`crane copy {{소스}} {{대상}} {{[-a|--all-tags]}}`

- 최대 동시 복사본 수를 설정, 기본값은 GOMAXPROCS:

`crane copy {{소스}} {{대상}} {{[-j|--jobs]}} {{int}}`

- 대상의 기존 태그를 덮어쓰지 않음:

`crane copy {{소스}} {{대상}} {{[-n|--no-clobber]}}`

- 도움말 표시:

`crane copy {{[-h|--help]}}`

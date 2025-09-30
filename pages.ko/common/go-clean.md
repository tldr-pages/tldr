# go clean

> 오브젝트 파일과 캐시 파일 제거.
> 더 많은 정보: <https://pkg.go.dev/cmd/go#hdr-Remove_object_files_and_cached_files>.

- 실제로 제거하지 않고 제거 명령 출력:

`go clean -n`

- 빌드 캐시 삭제:

`go clean -cache`

- 모든 캐시된 테스트 결과 삭제:

`go clean -testcache`

- 모듈 캐시 삭제:

`go clean -modcache`

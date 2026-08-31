# uv cache

> `uv`의 전역 캐시 디렉터리를 관리.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-cache>.

- 캐시 디렉터리 경로 표시:

`uv cache dir`

- 전체 캐시 삭제 (캐시된 모든 패키지와 환경 제거):

`uv cache clean`

- 지정한 패키지의 캐시 삭제:

`uv cache clean {{패키지1 패키지2 ...}}`

- 캐시에서 더 이상 참조되지 않는 모든 객체 제거:

`uv cache prune`

- GitHub Actions 등의 CI 환경에 최적화하여 캐시 정리:

`uv cache prune --ci`

- 지정한 캐시 디렉터리 사용:

`uv cache clean --cache-dir {{경로/대상/캐시}}`

- 자세한 출력을 표시하며 캐시 삭제:

`uv cache clean {{[-v|--verbose]}}`

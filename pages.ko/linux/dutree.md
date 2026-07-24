# dutree

> 컬러 텍스트 기반 트리 형태로 파일 시스템 사용량을 분석.
> 더 많은 정보: <https://github.com/nachoparker/dutree#usage>.

- 현재 디렉터리의 트리 형태 사용량 표시:

`dutree`

- 지정한 디렉터리의 사용량 표시:

`dutree {{경로/대상/디렉터리}}`

- 지정한 크기(KB - K, MB - M, GB - G)보다 작은 항목을 하나로 묶어 표시:

`dutree --aggr {{숫자}}K`

- 지정한 깊이까지 하위 디렉터리 표시 (기본값: 1):

`dutree --depth {{깊이}}`

- 파일만 표시하여 빠르게 개요 확인:

`dutree --files-only`

- 숨김 파일 제외:

`dutree --no-hidden`

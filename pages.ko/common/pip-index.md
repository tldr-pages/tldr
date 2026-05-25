# pip index

> 패키지 인덱스에서 사용 가능한 정보 조회.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_index/>.

- 특정 패키지의 사용 가능한 모든 버전 목록 표시:

`pip index versions {{패키지}}`

- 특정 인덱스에서 버전 목록 표시:

`pip index versions {{패키지}} --index-url {{https://test.pypi.org/simple/}}`

- 프리릴리스(pre-release) 버전 포함:

`pip index versions {{패키지}} --pre`

- 추가 인덱스 포함:

`pip index versions {{패키지}} --extra-index-url {{https://example.com/simple/}}`

- 특정 플랫폼용 버전 목록 표시:

`pip index versions {{패키지}} --platform {{linux_x86_64}}`

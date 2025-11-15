# gcrane gc

> 태그가 지정되지 않은 이미지를 나열.
> 가비지 수집이 가능한 이미지를 계산.
> `gcrane delete`로 구성하여 실제로 가비지 수집할 수 있음.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 태그가 지정되지 않은 이미지 목록:

`gcrane gc {{레포지토리}}`

- 레포지토리를 통해 반복할지 여부:

`gcrane gc {{레포지토리}} {{[-r|--recursive]}}`

- 도움말 표시:

`gcrane gc {{[-h|--help]}}`

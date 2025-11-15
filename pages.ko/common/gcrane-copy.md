# gcrane copy

> 다이제스트 값을 유지하며 소스에서 대상으로 원격 이미지를 효율적으로 복사.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 소스에서 대상으로 이미지 복사:

`gcrane {{[cp|copy]}} {{소스}} {{대상}}`

- 최대 동시 복사본 수를 설정, 기본값은 20:

`gcrane copy {{소스}} {{대상}} {{[-j|--jobs]}} {{nr_of_copies}}`

- 레포지토리를 통해 반복할지 여부 문의:

`grance copy {{소스}} {{대상}} {{[-r|--recursive]}}`

- 도움말 표시:

`gcrane copy {{[-h|--help]}}`

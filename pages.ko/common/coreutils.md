# coreutils

> Uutils coreutils는 Rust 언어로 작성된 GNU coreutils의 크로스 플랫폼 재구현.
> Uutils는 하나의 멀티콜 바이너리에서 여러 유틸리티를 실행할 수 있도록 하여, 전체 바이너리 크기를 줄이며 이식성을 높여줍니다.
> 더 많은 정보: <https://uutils.github.io/coreutils/docs/multicall.html>.

- 유틸리티와 옵션을 함께 실행:

`coreutils {{유틸}} {{유틸_옵션}}`

- 파일을 긴([l]ong) 형식으로 출력:

`coreutils ls -l`

- `ls` 도움말 출력:

`coreutils ls --help`

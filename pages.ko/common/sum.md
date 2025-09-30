# sum

> 파일의 체크섬과 블록 수를 계산.
> 더 현대적인 `cksum`의 전신.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sum-invocation.html>.

- BSD 호환 알고리즘과 1024바이트 블록으로 체크섬 계산:

`sum {{경로/대상/파일}}`

- System V 호환 알고리즘과 512바이트 블록으로 체크섬 계산:

`sum {{[-s|--sysv]}} {{경로/대상/파일}}`

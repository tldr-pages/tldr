# pbpaste

> 클립보드의 내용을 `stdout`으로 전송.
> 키보드에서 `<Cmd v>`를 누르는 것과 유사.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/pbcopy.1>.

- 클립보드의 내용을 [f]파일에 쓰기:

`pbpaste > {{경로/대상/파일}}`

- 클립보드의 내용을 명령어의 입력으로 사용:

`pbpaste | grep foo`

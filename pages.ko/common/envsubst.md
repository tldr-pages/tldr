# envsubst

> 환경변수를 쉘 형식 문자열의 값으로 대체.
> 교체할 변수는 `${var}` 또는 `$var` 형식이어야 함.
> 더 많은 정보: <https://www.gnu.org/software/gettext/manual/gettext.html#envsubst-Invocation>.

- `stdin`의 환경 변수를 바꾸고 `stdout`으로 출력:

`echo '{{$HOME}}' | envsubst`

- 입력 파일의 환경 변수를 바꾸고 `stdout`으로 출력:

`envsubst < {{경로/대상/입력_파일}}`

- 입력 파일의 환경 변수를 바꾸고 파일로 출력:

`envsubst < {{경로/대상/입력_파일}} > {{경로/대상/출력_파일}}`

- 공백으로 구분된 목록에서 입력 파일의 환경 변수를 변경:

`envsubst < {{경로/대상/입력_파일}} '{{$USER $SHELL $HOME}}'`

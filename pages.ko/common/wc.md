# wc

> 줄 단어 및 바이트 수 계산.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- 파일의 모든 줄 수 계산:

`wc {{[-l|--lines]}} {{경로/대상/파일}}`

- 파일의 모든 단어 수 계산:

`wc {{[-w|--words]}} {{경로/대상/파일}}`

- 파일의 모든 바이트 수 계산:

`wc {{[-c|--bytes]}} {{경로/대상/파일}}`

- 파일의 모든 문자 수 계산(멀티바이트 문자 고려):

`wc {{[-m|--chars]}} {{경로/대상/파일}}`

- `stdin`의 모든 줄, 단어 및 바이트 수를 계산:

`{{find .}} | wc`

- 가장 긴 줄의 길이를 문자 수로 계산:

`wc {{[-L|--max-line-length]}} {{경로/대상/파일}}`

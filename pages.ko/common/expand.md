# expand

> 탭을 공백으로 변환.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- 각 파일의 탭을 공백으로 변환하여 `stdout`에 작성:

`expand {{경로/대상/파일}}`

- `stdin`에서 읽어 탭을 공백으로 변환:

`expand`

- 공백이 아닌 경우 탭을 변환하지 않음:

`expand -i {{경로/대상/파일}}`

- 탭을 8자가 아닌 특정 수의 문자 간격으로 위치:

`expand -t {{숫자}} {{경로/대상/파일}}`

- 명시적인 탭 위치를 쉼표로 구분한 목록을 사용:

`expand -t {{1,4,6}}`

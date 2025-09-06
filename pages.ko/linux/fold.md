# fold

> 고정 폭 출력 장치를 위한 긴 줄을 접습니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- 고정 폭으로 줄을 접기:

`fold {{[-w|--width]}} {{폭}} {{경로/대상/파일}}`

- 바이트 단위로 폭 계산 (기본값은 열 단위로 계산):

`fold {{[-b|--bytes]}} {{[-w|--width]}} {{바이트_단위_폭}} {{경로/대상/파일}}`

- 폭 제한 내에서 가장 오른쪽 공백 뒤에서 줄을 나누기:

`fold {{[-s|--spaces]}} {{[-w|--width]}} {{폭}} {{경로/대상/파일}}`

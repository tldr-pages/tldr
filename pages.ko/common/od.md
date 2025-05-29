# od

> 파일 내용을 8진수, 10진수 또는 16진수 형식으로 표시.
> 선택적으로 각 줄에 대한 바이트 오프셋 및/또는 인쇄 가능한 표현을 표시.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- 기본 설정으로 파일 표시: 8진수 형식, 8바이트 단위로 줄바꿈, 8진수 바이트 오프셋, 중복 줄은 `*`로 대체:

`od {{경로/대상/파일}}`

- 자세한 모드로 파일 표시, 즉 중복 줄을 `*`로 대체하지 않음:

`od {{[-v|--output-duplicates]}} {{경로/대상/파일}}`

- 16진수 형식(2바이트 단위)으로 파일 표시, 10진수 형식의 바이트 오프셋:

`od {{[-t|--format]}} {{x}} {{[-A|--address-radix]}} {{d}} {{[-v|--output-duplicates]}} {{경로/대상/파일}}`

- 16진수 형식(1바이트 단위)으로 파일 표시, 4바이트 단위로 줄바꿈:

`od {{[-t|--format]}} {{x1}} {{[-w|--width=]}}4 {{[-v|--output-duplicates]}} {{경로/대상/파일}}`

- 16진수 형식과 문자 표현으로 파일 표시, 바이트 오프셋은 출력하지 않음:

`od {{[-t|--format]}} {{xz}} {{[-A|--address-radix]}} {{n}} {{[-v|--output-duplicates]}} {{경로/대상/파일}}`

- 500번째 바이트부터 시작하여 파일의 100바이트만 읽기:

`od {{[-N|--read-bytes]}} 100 {{[-j|--skip-bytes]}} 500 {{[-v|--output-duplicates]}} {{경로/대상/파일}}`

# head

> 파일의 첫 부분을 출력합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- 파일의 처음 몇 줄을 출력:

`head {{[-n|--lines]}} {{개수}} {{경로/대상/파일}}`

- 파일의 처음 몇 바이트를 출력:

`head {{[-c|--bytes]}} {{개수}} {{경로/대상/파일}}`

- 파일의 마지막 몇 줄을 제외하고 출력:

`head {{[-n|--lines]}} -{{개수}} {{경로/대상/파일}}`

- 파일의 마지막 몇 바이트를 제외하고 출력:

`head {{[-c|--bytes]}} -{{개수}} {{경로/대상/파일}}`

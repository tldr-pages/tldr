# cython

> `.pyx` 파일을 C 또는 C++ 소스 파일로 변환하는 컴파일러.
> 더 많은 정보: <https://docs.cython.org/en/latest/>.

- C 코드로 컴파일:

`cython {{경로/대상/파일}}`

- C++ 코드로 컴파일:

`cython --cplus {{경로/대상/파일}}`

- 출력 파일을 지정:

`cython {{[-o|--output-file]}} {{경로/대상/출력_파일}} {{경로/대상/파일}}`

- 버전 표시:

`cython {{[-V|--version]}}`

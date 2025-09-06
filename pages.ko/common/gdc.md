# gdc

> GCC를 백엔드로 사용하는 D 컴파일러.
> 더 많은 정보: <https://wiki.dlang.org/Using_GDC>.

- 실행 파일을 생성:

`gdc {{경로/대상/소스.d}} -o {{경로/대상/출력_실행파일}}`

- 모듈 종속성에 대한 정보를 출력:

`gdc -fdeps`

- Ddoc 문서를 생성:

`gdc -fdoc`

- D 인터페이스 파일 생성:

`gdc -fintfc`

- 컴파일 시 표준 GCC 라이브러리를 링크하지 않음:

`gdc -nostdlib`

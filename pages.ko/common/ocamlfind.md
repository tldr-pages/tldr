# ocamlfind

> OCaml을 위한 findlib 패키지 관리자.
> 외부 라이브러리로 실행 파일을 연결하는 과정을 단순화합니다.
> 더 많은 정보: <https://manned.org/ocamlfind>.

- 소스 파일을 네이티브 바이너리로 컴파일하고 패키지와 링크:

`ocamlfind ocamlopt -package {{패키지1}},{{패키지2}} -linkpkg -o {{경로/대상/실행파일}} {{경로/대상/소스.ml}}`

- 소스 파일을 바이트코드 바이너리로 컴파일하고 패키지와 링크:

`ocamlfind ocamlc -package {{패키지1}},{{패키지2}} -linkpkg -o {{경로/대상/실행파일}} {{경로/대상/소스.ml}}`

- 다른 플랫폼용으로 크로스 컴파일:

`ocamlfind -toolchain {{크로스_툴체인}} ocamlopt -o {{경로/대상/실행파일}} {{경로/대상/소스.ml}}`

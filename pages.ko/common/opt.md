# opt

> LLVM 소스 파일을 최적화하고 분석합니다.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/opt.html>.

- 비트코드 파일에 최적화 또는 분석 실행:

`opt -{{패스명}} {{경로/대상/파일.bc}} -S -o {{파일_opt.bc}}`

- 함수의 제어 흐름 그래프를 `.dot` 파일로 출력:

`opt {{-dot-cfg}} -S {{경로/대상/파일.bc}} -disable-output`

- 프로그램을 2단계로 최적화하고 결과를 다른 파일로 출력:

`opt -O2 {{경로/대상/파일.bc}} -S -o {{경로/대상/출력_파일.bc}}`

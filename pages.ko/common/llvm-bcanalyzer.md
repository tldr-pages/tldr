# llvm-bcanalyzer

> LLVM Bitcode (`.bc`) 분석기.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Bitcode 파일에 대한 통계 출력:

`llvm-bcanalyzer {{경로/대상/파일.bc}}`

- Bitcode 파일에 대한 SGML 표현과 통계 출력:

`llvm-bcanalyzer -dump {{경로/대상/파일.bc}}`

- `stdin`에서 Bitcode 파일을 읽고 분석:

`cat {{경로/대상/파일.bc}} | llvm-bcanalyzer`

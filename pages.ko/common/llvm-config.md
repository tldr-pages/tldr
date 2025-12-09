# llvm-config

> LLVM을 사용하는 프로그램을 컴파일하는 데 필요한 다양한 구성 정보를 얻습니다.
> 일반적으로 Makefile이나 configure 스크립트와 같은 빌드 시스템에서 호출됩니다.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- LLVM 기반 프로그램을 컴파일하고 링크:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{경로/대상/출력_실행파일}} {{경로/대상/소스.cc}}`

- LLVM 설치의 `PREFIX` 출력:

`llvm-config --prefix`

- LLVM 빌드에서 지원하는 모든 대상 출력:

`llvm-config --targets-built`

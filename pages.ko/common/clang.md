# clang

> C, C++, Objective-C 소스 파일을 컴파일. 수정 없이 GCC 대체(drop-in replacement)로 사용할 수 있음.
> LLVM의 일부.
> 더 많은 정보: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- 여러 소스 파일을 하나의 실행 파일로 컴파일:

`clang {{경로/대상/소스1.c 경로/대상/소스2.c ...}} {{[-o|--output]}} {{경로/대상/결과_실행파일}}`

- 모든 오류 및 경고 출력 활성화:

`clang {{경로/대상/소스.c}} -Wall {{[-o|--output]}} {{결과_실행파일}}`

- 일반적인 경고 표시, 디버그 심볼 포함, 디버깅에 영향을 주지 않는 최적화 적용:

`clang {{경로/대상/소스.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{경로/대상/결과_실행파일}}`

- 다른 경로의 라이브러리 및 헤더 포함:

`clang {{경로/대상/소스.c}} {{[-o|--output]}} {{경로/대상/결과_실행파일}} -I{{경로/대상/header}} -L{{경로/대상/라이브러리}} -l{{라이브러리_이름}}`

- 소스 코드를 LLVM 중간 표현(IR)으로 컴파일:

`clang {{[-S|--assemble]}} -emit-llvm {{경로/대상/소스.c}} {{[-o|--output]}} {{경로/대상/출력파일.ll}}`

- 소스 코드를 링킹 없이 오브젝트 파일로 컴파일:

`clang {{[-c|--compile]}} {{경로/대상/소스.c}}`

- 성능 최적화를 적용해 컴파일:

`clang {{경로/대상/소스.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{경로/대상/결과_실행파일}}`

- 버전 정보 표시:

`clang --version`

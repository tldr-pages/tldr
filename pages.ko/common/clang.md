# clang

> C, C++ 그리고 Objective-C 소스 파일을 위한 컴파일러입니다. GCC의 드롭인 대체로 사용할 수 있습니다.
> 더 많은 정보: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- 소스 코드를 실행 가능한 바이너리 파일로 컴파일합니다:

`clang {{입력_소스.c}} -o {{출력_실행가능파일}}`

- 모든 에러와 경고 메시지를 출력하도록 활성화합니다:

`clang {{입력_소스.c}} -Wall -o {{출력_실행가능파일}}`

- 소스 파일과 다른 경로에 있는 라이브러리를 포함합니다:

`clang {{입력_소스.c}} -o {{출력_실행가능파일}} -I{{헤더_경로}} -L{{라이브러리_경로}} -l{{라이브러리명}}`

- 소스 코드를 LLVM Intermediate Representation(IR)로 컴파일 합니다:

`clang -S -emit-llvm {{파일.c}} -o {{파일.ll}}`

- 소스 코드를 링킹 없이 컴파일합니다:

`clang -c {{입력_소스.c}}`

# clang-format

> C/C++/Java/JavaScript/Objective-C/Protobuf/C# 코드 자동 형식화.
> 더 많은 정보: <https://clang.llvm.org/docs/ClangFormat.html>.

- 파일 형식을 지정하고 결과를 `stdout`으로 출력:

`clang-format {{경로/대상/파일}}`

- 그 자리에서 파일 형식을 지정:

`clang-format -i {{경로/대상/파일}}`

- 미리 정의된 코딩 스타일을 사용하여 파일 형식을 지정:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{경로/대상/파일}}`

- 소스 파일의 상위 디렉터리 중 하나에 있는 `.clang-format` 파일을 사용하여 파일 형식을 지정:

`clang-format --style=file {{경로/대상/파일}}`

- 사용자 정의 `.clang-format` 파일을 생성:

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`

# clang-tidy

> 정적 분석을 통해 스타일 위반, 버그 및 보안 결함을 찾는 LLVM 기반 C/C++ 린트 프로그램입니다.
> 더 많은 정보: <https://clang.llvm.org/extra/clang-tidy/>.

- 소스 파일에 대한 기본 검사를 실행:

`clang-tidy {{경로/대상/파일.cpp}}`

- 파일에 대해 `cppcoreguidelines` 검사 이외의 검사를 실행하지 않음:

`clang-tidy {{경로/대상/파일.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- 사용 가능한 모든 검사를 나열:

`clang-tidy -checks={{*}} -list-checks`

- 컴파일 옵션으로 정의 및 포함을 지정 (`--` 뒤에서):

`clang-tidy {{경로/대상/파일.cpp}} -- -I{{내_프로젝트/포함}} -D{{정의}}`

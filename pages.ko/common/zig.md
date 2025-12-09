# zig

> Zig 컴파일러 및 툴체인.
> 더 많은 정보: <https://ziglang.org/documentation/master/>.

- 현재 디렉토리의 프로젝트 컴파일:

`zig build`

- 현재 디렉토리의 프로젝트 컴파일 및 실행:

`zig build run`

- `zig build` 애플리케이션 초기화:

`zig init-exe`

- `zig build` 라이브러리 초기화:

`zig init-lib`

- 테스트 빌드 생성 및 실행:

`zig test {{경로/대상/파일.zig}}`

- Zig 소스 코드를 표준 형식으로 재포맷:

`zig fmt {{경로/대상/파일.zig}}`

- Zig를 C 컴파일러로 사용:

`zig cc {{경로/대상/파일.c}}`

- Zig를 C++ 컴파일러로 사용:

`zig c++ {{경로/대상/파일.cpp}}`

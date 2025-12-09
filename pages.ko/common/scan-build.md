# scan-build

> 코드베이스에 정적 분석기를 실행하여 정기 빌드의 일부로 사용하는 명령줄 도구.
> 더 많은 정보: <https://clang-analyzer.llvm.org/scan-build.html>.

- 현재 디렉터리에서 프로젝트를 빌드하고 분석:

`scan-build {{make}}`

- 명령을 실행하고 모든 후속 옵션을 해당 명령에 전달:

`scan-build {{명령어}} {{명령어_인수들}}`

- 도움말 표시:

`scan-build`

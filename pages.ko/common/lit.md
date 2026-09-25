# lit

> LLVM과 Clang 스타일 테스트 스위트를 실행하고 결과를 유약하기 위한 LLVM 통합 테스트 도구.
> LLVM의 일부.
> 더 많은 정보: <https://www.llvm.org/docs/CommandGuide/lit.html>.

- 지정한 테스트 케이스 실행:

`lit {{경로/대상/테스트_파일.test}}`

- 지정한 디렉터리의 모든 테스트 케이스 실행:

`lit {{경로/대상/테스트_스위트}}`

- 모든 테스트를 실행하고 각 테스트의 실행 시간을 측정해, 요약 보고서를 출력:

`lit {{경로/대상/테스트_스위트}} --time-tests`

- Valgrind를 사용하여 개별 테스트 실행 (메모리 오류 및 메모리 누수 검사 포함):

`lit {{경로/대상/테스트_파일.test}} --vg --vg-leak --vg-args={{valgrind에_전송될_인자}}`

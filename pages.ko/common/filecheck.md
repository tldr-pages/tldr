# FileCheck

> 유연한 패턴 매칭 기반 파일검증 도구.
> 주로 LLVM 회귀 테스트에서 사용되며, `lit` 테스트의 일부로 활용됨.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/FileCheck.html>.

- `input_file` 내용을 `check_file`의 패턴과 비교:

`FileCheck --input-file={{path/to/input_file}} {{경로/대상/체크_파일}}`

- `stdin` 입력을 `check_file` 패턴과 비교:

`echo "{{일부_텍스트}}" | FileCheck {{경로/대상/체크_파일}}`

- 사용자 지정 체크 접두사 `prefix`로 매칭 (참고: 기본 접두사 `CHECK`):

`echo "{{일부_텍스트}}" | FileCheck --check-prefix={{prefix}} {{경로/대상/체크_파일}}`

- 정상 매칭된 패턴을 출력:

`echo "{{일부_텍스트}}" | FileCheck -v {{경로/대상/체크_파일}}`

- `llvm_code.ll`을 llvm-as로 처리 후 결과를 FileCheck로 검증:

`llvm-as {{path/to/llvm_code.ll}} | FileCheck {{경로/대상/체크_파일}}`

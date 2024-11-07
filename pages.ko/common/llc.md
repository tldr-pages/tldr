# llc

> LLVM 중간 표현(IR) 또는 비트코드를 대상에 맞는 어셈블리 언어로 컴파일합니다.
> 더 많은 정보: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- 비트코드 또는 IR 파일을 동일한 기본 이름의 어셈블리 파일로 컴파일:

`llc {{경로/대상/파일.ll}}`

- 모든 최적화 활성화:

`llc -O3 {{경로/대상/입력.ll}}`

- 특정 파일로 어셈블리 출력:

`llc --output {{경로/대상/출력.s}}`

- 완전히 재배치 가능하고 위치 독립적인 코드 생성:

`llc -relocation-model=pic {{경로/대상/입력.ll}}`

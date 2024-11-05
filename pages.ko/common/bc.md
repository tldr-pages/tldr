# bc

> 임의의 정밀 계산기 언어.
> 참조: `dc`, `qalc`.
> 더 많은 정보: <https://manned.org/bc>.

- 대화형 세션을 시작:

`bc`

- 표준 수학 라이브러리([l]ibrary)가 활성화된 상태에서 대화형([i]nteractive) 세션을 시작:

`bc --interactive --mathlib`

- 표현식을 계산:

`echo '{{5 / 3}}' | bc`

- 스크립트 실행:

`bc {{경로/대상/스크립트.bc}}`

- 지정된 척도를 사용해 표현식을 계산:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- `mathlib`을 사용하여 사인/코사인/아크탄젠트/자연 로그/지수 함수를 계산:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- 인라인 계승 스크립트를 실행:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`

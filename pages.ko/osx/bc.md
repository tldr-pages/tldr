# bc

> 임의 정밀도 계산기 언어.
> 같이 보기: `dc`.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- 대화형 세션 시작:

`bc`

- 표준 수학 라이브러리를 활성화하여 대화형 세션 시작:

`bc --mathlib`

- 수식 계산:

`bc --expression '{{5 / 3}}'`

- 스크립트 실행:

`bc {{경로/대상/스크립트.bc}}`

- 지정된 스케일로 수식 계산:

`bc --expression '{{scale = 10; 5 / 3}}'`

- `mathlib`을 사용하여 사인/코사인/아크탄젠트/자연 로그/지수 함수 계산:

`bc --mathlib --expression '{{s|c|a|l|e}}({{1}})'`

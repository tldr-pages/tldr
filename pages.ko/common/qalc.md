# qalc

> 강력하고 사용하기 쉬운 명령줄 계산기.
> 같이 보기: `bc`.
> 더 많은 정보: <https://qalculate.github.io/manual/qalc.html>.

- [i]nteractive 모드로 시작:

`qalc {{--interactive}}`

- [t]erse 모드로 시작 (결과만 출력):

`qalc --terse`

- 통화 환율 [e] 갱신:

`qalc --exrates`

- 비대화식으로 계산 수행:

`qalc {{66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...}}`

- 지원되는 모든 함수/접두사/단위/변수 나열:

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- [f]ile에서 명령 실행:

`qalc --file {{경로/대상/파일}}`

# hledger add

> 콘솔에서 대화형 프롬프트로 새로운 거래를 기록합니다.
> 더 많은 정보: <https://hledger.org/hledger.html#add>.

- 기본 저널 파일에 새로운 거래 기록:

`hledger add`

- `2024.journal`에 거래를 추가하되, 자동 완성을 위해 `2023.journal`도 로드:

`hledger add --file {{경로/대상/2024.journal}} --file {{경로/대상/2023.journal}}`

- 처음 네 개의 프롬프트에 대한 답변 제공:

`hledger add {{오늘}} '{{best buy}}' {{지출:용품}} '{{$20}}'`

- `$PAGER`로 `add`의 옵션 및 문서 보기:

`hledger add --help`

- 사용 가능하면 `info` 또는 `man`으로 `add`의 문서 보기:

`hledger help add`

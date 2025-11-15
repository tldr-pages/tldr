# rgpt

> 터미널에서 바로 사용할 수 있는 GPT 기반 자동 코드 리뷰 도구.
> 더 많은 정보: <https://github.com/vibovenkat123/review-gpt>.

- 추가 옵션 없이 GPT에게 코드 개선 요청:

`rgpt --i "$(git diff {{경로/대상/파일}})"`

- 코드 리뷰 중 `rgpt`에서 더 자세한 출력 얻기:

`rgpt --v --i "$(git diff {{경로/대상/파일}})"`

- GPT에게 코드 개선 요청 및 GPT3 토큰 수를 특정 수로 제한하기:

`rgpt --max {{300}} --i "$(git diff {{경로/대상/파일}})"`

- 0에서 2 사이의 실수값을 사용하여 더 독특한 결과 요청 (높을수록 더 독특함):

`rgpt --pres {{1.2}} --i "$(git diff {{경로/대상/파일}})"`

- 특정 모델을 사용하여 코드 리뷰 요청:

`rgpt --model {{davinci}} --i "$(git diff {{경로/대상/파일}})"`

- `rgpt`를 사용하여 JSON 출력 생성:

`rgpt --json --i "$(git diff {{경로/대상/파일}})"`

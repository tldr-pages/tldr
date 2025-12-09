# rubocop

> Ruby 파일을 린트합니다.
> 더 많은 정보: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- 현재 디렉토리의 모든 파일 확인(하위 디렉토리 포함):

`rubocop`

- 하나 이상의 특정 파일 또는 디렉토리 확인:

`rubocop {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`

- 출력 결과를 파일에 저장:

`rubocop --out {{경로/대상/파일}}`

- cop(린터 규칙) 목록 보기:

`rubocop --show-cops`

- 특정 cop 제외:

`rubocop --except {{cop1 cop2 ...}}`

- 지정된 cop만 실행:

`rubocop --only {{cop1 cop2 ...}}`

- 파일 자동 수정(실험적 기능):

`rubocop --auto-correct`

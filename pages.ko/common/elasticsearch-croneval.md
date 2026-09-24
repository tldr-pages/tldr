# elasticsearch-croneval

> `cron` 표현식을 검증 및 실행 결과를 평가하는 도구. Elasticsearch에서 사용할 수 있는 `cron` 표현식의 유효성을 확인 후 예상 실행 결과를 검증하는 데 사용됨.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-croneval>.

- `cron` 표현식을 평가하고 다음 10개 실행 시간 출력 (기본 동작):

`elasticsearch-croneval "{{cron_표현식}}"`

- `cron` 표현식을 평가하고 지정한 개수만큼 미래에 실행될 시간 출력:

`elasticsearch-croneval "{{cron_표현식}}" {{[-c|--count]}} {{정수}}`

- 잘못된 `cron` 표현식에 대해 상세 정보(스택 트레이스 포함)출력:

`elasticsearch-croneval "{{invalid_cron_표현식}}" {{[-d|--detail]}}`

- 최소 출력 표시 (silent 모드):

`elasticsearch-croneval "{{cron_표현식}}" {{[-s|--silent]}}`

- 상세 출력 표시:

`elasticsearch-croneval "{{cron_표현식}}" {{[-v|--verbose]}}`

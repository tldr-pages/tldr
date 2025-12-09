# sort

> 텍스트 파일의 줄을 정렬합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- 파일을 오름차순으로 정렬:

`sort {{경로/대상/파일}}`

- 파일을 내림차순으로 정렬:

`sort {{[-r|--reverse]}} {{경로/대상/파일}}`

- 파일을 대소문자를 구분하지 않고 정렬:

`sort {{-f|--ignore-case}} {{경로/대상/파일}}`

- 파일을 알파벳 순이 아닌 숫자 순으로 정렬:

`sort {{[-n|--numeric-sort]}} {{경로/대상/파일}}`

- ":"를 필드 구분자로 사용하여 3번째 필드를 기준으로 `/etc/passwd`를 숫자 순으로 정렬:

`sort {{[-t|--field-separator]}} {{:}} {{[-k|--key]}} {{3n}} {{/etc/passwd}}`

- 위와 동일하지만, 3번째 필드의 항목이 동일한 경우 4번째 필드를 지수와 함께 숫자 순으로 정렬:

`sort {{[-t|--field-separator]}} {{:}} {{[-k|--key]}} {{3,3n}} {{[-k|--key]}} {{4,4g}} {{/etc/passwd}}`

- 파일을 정렬하면서 유일한 줄만 보존:

`sort {{[-u|--unique]}} {{경로/대상/파일}}`

- 파일을 정렬하여 지정된 출력 파일에 출력 (원본 파일을 직접 정렬할 때 사용 가능):

`sort {{[-o|--output]}} {{경로/대상/파일}} {{경로/대상/파일}}`

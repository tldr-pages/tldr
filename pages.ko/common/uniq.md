# uniq

> 입력 또는 파일에서 고유한 줄을 출력합니다.
> 인접하지 않은 반복 줄을 감지하지 않으므로 먼저 정렬해야 합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- 각 줄을 한 번씩만 표시:

`sort {{경로/대상/파일}} | uniq`

- 고유한 줄만 표시:

`sort {{경로/대상/파일}} | uniq {{[-u|--unique]}}`

- 중복된 줄만 표시:

`sort {{경로/대상/파일}} | uniq {{[-d|--repeated]}}`

- 각 줄의 발생 횟수와 함께 해당 줄 표시:

`sort {{경로/대상/파일}} | uniq {{[-c|--count]}}`

- 각 줄의 발생 횟수를 표시하고, 가장 자주 발생한 순서로 정렬:

`sort {{경로/대상/파일}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`

# unexpand

> 공백을 탭으로 변환.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/unexpand-invocation.html>.

- 각 파일의 공백을 탭으로 변환하여 `stdout`에 출력:

`unexpand {{경로/대상/파일}}`

- `stdout`에서 읽어온 공백을 탭으로 변환:

`unexpand`

- 처음의 공백만이 아닌 모든 공백을 변환:

`unexpand -a {{경로/대상/파일}}`

- 앞부분의 공백 시퀀스만 변환 (옵션 -a를 무시):

`unexpand --first-only {{경로/대상/파일}}`

- 탭을 8칸이 아닌 지정한 문자 수만큼 떨어뜨려 변환 (-a 활성화):

`unexpand -t {{숫자}} {{경로/대상/파일}}`

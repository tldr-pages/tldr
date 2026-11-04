# tqdm

> 명령의 실행 진행 상황을 시간에 따라 표시.
> 더 많은 정보: <https://tqdm.github.io/docs/cli/>.

- 초당 반복 횟수를 표시하고 이후 출력을 `stdout`으로 전달:

`{{seq 10000000}} | tqdm | {{명령어}}`

- 진행률 표시줄 생성:

`{{seq 10000000}} | tqdm --total {{10000000}} | {{명령어}}`

- 디렉터리를 압축하면서 파일 개수를 기준으로 진행률 표시줄 생성:

`zip {{[-r|--recurse-paths]}} {{경로/대상/아카이브.zip}} {{경로/대상/디렉터리}} | tqdm --total $(find {{경로/대상/디렉터리}} | wc {{[-l|--lines]}}) --unit files --null`

- tar로 아카이브를 생성하면서 진행률 표시줄 표시 (시스템에 관계없이 동작, GNU tar는 `stdout`, BSD tar는 `stderr`를 사용):

`tar vzcf {{경로/대상/아카이브.tar.gz}} {{경로/대상/디렉터리}} 2>&1 | tqdm --total $(find {{경로/대상/디렉터리}} | wc {{[-l|--lines]}}) --unit files --null`

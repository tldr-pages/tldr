# git merge-index

> 병합이 필요한 파일에 대해 병합 프로그램 실행.
> 더 많은 정보: <https://git-scm.com/docs/git-merge-index>.

- 표준 헬퍼를 사용하여 병합이 필요한 모든 파일 병합:

`git merge-index git-merge-one-file -a`

- 특정 파일 병합:

`git merge-index git-merge-one-file -- {{경로/대상/파일}}`

- 실패가 발생해도 계속 진행하면서 여러 파일을 병합:

`git merge-index -o git-merge-one-file -- {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 사용자 지정 병합 프로그램으로 조용히 모든 파일 병합:

`git merge-index -q {{병합할_프로그램}} -a`

- `cat`을 사용해서 파일의 병합 입력 정보 확인:

`git merge-index cat -- {{경로}}`

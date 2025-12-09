# sshare

> 클러스터에 대한 연결의 공유 목록을 표시합니다.
> 더 많은 정보: <https://slurm.schedmd.com/sshare.html>.

- Slurm 공유 정보 나열:

`sshare`

- 출력 형식 제어:

`sshare --{{parsable|parsable2|json|yaml}}`

- 표시할 필드 제어:

`sshare --format={{형식_문자열}}`

- 지정된 사용자에 대한 정보만 표시:

`sshare --users={{사용자_ID_1,사용자_ID_2,...}}`

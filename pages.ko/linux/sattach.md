# sattach

> Slurm 작업 단계에 연결.
> 더 많은 정보: <https://slurm.schedmd.com/sattach.html>.

- Slurm 작업 단계의 IO 스트림(`stdout`, `stderr`, `stdin`)을 현재 터미널로 리디렉션:

`sattach {{작업_ID}}.{{단계_ID}}`

- 현재 콘솔의 입력을 지정된 작업의 `stdin`으로 사용:

`sattach --input-filter {{작업_번호}}`

- 지정된 작업의 `stdin`/`stderr`만 리디렉션:

`sattach --{{출력|오류}}-filter {{작업_번호}}`

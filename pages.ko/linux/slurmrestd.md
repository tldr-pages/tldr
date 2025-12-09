# slurmrestd

> REST API를 통해 Slurm에 인터페이스를 제공하는 도구입니다. *Inetd 모드* 및 *Listen 모드*에서 사용할 수 있습니다.
> 더 많은 정보: <https://slurm.schedmd.com/slurmrestd.html>.

- 클라이언트 요청을 처리하기 전에 그룹 ID를 변경하고 보조 그룹을 제거:

`slurmrestd --g {{그룹_ID}} {{[호스트]:포트 | unix:/경로/대상/소켓}}`

- 로드할 인증 플러그인의 쉼표로 구분된 목록:

`slurmrestd -a {{인증_플러그인}} {{[호스트]:포트 | unix:/경로/대상/소켓}}`

- 지정된 파일에서 Slurm 설정 읽기:

`slurmrestd -f {{경로/대상/파일}}`

- 클라이언트 요청을 처리하기 전에 사용자 ID 변경:

`slurmrestd -u {{사용자_ID}}`

- 도움말 표시:

`slurmrestd -h`

- 버전 표시:

`slurmrestd -V`

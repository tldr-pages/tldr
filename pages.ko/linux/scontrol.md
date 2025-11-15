# scontrol

> 작업에 대한 정보를 보고 수정합니다.
> 더 많은 정보: <https://slurm.schedmd.com/scontrol.html>.

- 작업에 대한 정보 표시:

`scontrol show job {{작업_ID}}`

- 쉼표로 구분된 실행 중인 작업 목록 일시 중지:

`scontrol suspend {{작업_ID1,작업_ID2,...}}`

- 쉼표로 구분된 일시 중지된 작업 목록 재개:

`scontrol resume {{작업_ID1,작업_ID2,...}}`

- 쉼표로 구분된 대기 중인 작업 목록 보류 (작업 예약을 허용하려면 `release` 명령 사용):

`scontrol hold {{작업_ID1,작업_ID2,...}}`

- 쉼표로 구분된 일시 중지된 작업 목록 해제:

`scontrol release {{작업_ID1,작업_ID2,...}}`

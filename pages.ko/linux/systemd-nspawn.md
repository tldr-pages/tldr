# systemd-nspawn

> 경량 컨테이너에서 명령이나 운영 체제를 실행.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html>.

- 컨테이너에서 명령 실행:

`systemd-nspawn --directory {{경로/대상/컨테이너_루트}}`

- 컨테이너에서 전체 Linux 기반 운영 체제 실행:

`systemd-nspawn --boot --directory {{경로/대상/컨테이너_루트}}`

- 지정된 명령을 컨테이너에서 PID 2로 실행 (PID 1 대신)하고, 초기화 프로세스 스텁 사용:

`systemd-nspawn --directory {{경로/대상/컨테이너_루트}} --as-pid2`

- 머신 이름과 호스트 이름 지정:

`systemd-nspawn --machine={{컨테이너_이름}} --hostname={{컨테이너_호스트}} --directory {{경로/대상/컨테이너_루트}}`

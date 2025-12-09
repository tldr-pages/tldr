# bpftool

> eBPF 프로그램 및 맵을 간단하게 검사하고 조작.
> `prog`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://manned.org/bpftool>.

- 로드된 `eBPF` 프로그램 정보 나열:

`bpftool prog list`

- 커널 네트워킹 하위 시스템의 `eBPF` 프로그램 연결 나열:

`bpftool net list`

- 모든 활성 링크 나열:

`bpftool link list`

- 시스템의 모든 `raw_tracepoint`, `tracepoint`, `kprobe` 연결 나열:

`bpftool perf list`

- `BPF Type Format (BTF)` 데이터 나열:

`bpftool btf list`

- 로드된 맵 정보 나열:

`bpftool map list`

- 네트워크 장치 "eth0"의 지원하는 `eBPF` 기능 검사:

`bpftool feature probe dev {{eth0}}`

- 파일에서 배치 모드로 명령 실행:

`bpftool batch file {{내_파일}}`

# numactl

> 프로세스 또는 공유 메모리에 대한 NUMA 정책 제어.
> 더 많은 정보: <https://manned.org/numactl>.

- 노드 0에서 명령을 실행하고 메모리는 노드 0과 1에 할당:

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{명령}} {{명령_인자들}}`

- 현재 CPU 세트의 CPU(코어) 0-4 및 8-12에서 명령 실행:

`numactl --physcpubind={{+0-4,8-12}} -- {{명령}} {{명령_인자들}}`

- 모든 CPU에 메모리를 인터리브하여 명령 실행:

`numactl --interleave={{all}} -- {{명령}} {{명령_인자들}}`

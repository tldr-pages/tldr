# salloc

> 클러스터에서 하나 이상의 노드를 할당하여 대화형 셸 세션을 시작하거나 명령을 실행합니다.
> 더 많은 정보: <https://slurm.schedmd.com/salloc.html>.

- 클러스터의 노드에서 대화형 셸 세션 시작:

`salloc`

- 클러스터의 노드에서 지정된 명령을 동기적으로 실행:

`salloc {{ls -a}}`

- 지정된 제약 조건을 충족하는 노드만 할당:

`salloc --constraint={{(amd|intel)&gpu}}`

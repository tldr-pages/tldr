# cgcreate

> cgroup을 생성하여 프로세스가 사용하는 자원을 제한, 측정 및 제어.
> `cgroups`의 유형은 `memory`, `cpu`, `net_cls` 등이 있습니다.
> 더 많은 정보: <https://manned.org/cgcreate>.

- 새 그룹 생성:

`cgcreate -g {{그룹_유형}}:{{그룹_이름}}`

- 여러 cgroup 유형으로 새 그룹 생성:

`cgcreate -g {{그룹_유형1}},{{그룹_유형2}}:{{그룹_이름}}`

- 하위 그룹 생성:

`mkdir /sys/fs/cgroup/{{그룹_유형}}/{{그룹_이름}}/{{하위_그룹_이름}}`

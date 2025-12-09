# cgexec

> 프로세스가 사용하는 자원을 제한, 측정 및 제어.
> `cpu`, `memory` 등 여러 cgroup 유형(컨트롤러)이 존재합니다.
> 더 많은 정보: <https://manned.org/cgexec>.

- 지정된 컨트롤러와 cgroup에서 프로세스를 실행:

`cgexec -g {{컨트롤러}}:{{cgroup_이름}} {{프로세스_이름}}`

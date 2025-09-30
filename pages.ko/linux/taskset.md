# taskset

> 프로세스의 CPU 친화도를 가져오거나 설정하거나 정의된 CPU 친화도로 새 프로세스를 시작합니다.
> 더 많은 정보: <https://manned.org/taskset>.

- 실행 중인 프로세스의 PID로 CPU 친화도 가져오기:

`taskset --pid --cpu-list {{pid}}`

- 실행 중인 프로세스의 PID로 CPU 친화도 설정:

`taskset --pid --cpu-list {{cpu_id}} {{pid}}`

- 단일 CPU에 대한 친화도로 새 프로세스 시작:

`taskset --cpu-list {{cpu_id}} {{명령어}}`

- 여러 비연속 CPU에 대한 친화도로 새 프로세스 시작:

`taskset --cpu-list {{cpu_id_1}},{{cpu_id_2}},{{cpu_id_3}}`

- CPU 1부터 4까지의 친화도로 새 프로세스 시작:

`taskset --cpu-list {{cpu_id_1}}-{{cpu_id_4}}`

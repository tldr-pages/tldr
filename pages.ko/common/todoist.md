# todoist

> 명령줄에서 <https://todoist.com>에 접근하세요.
> 더 많은 정보: <https://github.com/sachaos/todoist>.

- 작업 추가:

`todoist add "{{작업_이름}}"`

- 라벨, 프로젝트 및 기한이 있는 높은 우선순위 작업 추가:

`todoist add "{{작업_이름}}" --priority {{1}} --label-ids "{{라벨_ID}}" --project-name "{{프로젝트_이름}}" --date "{{tmr 9am}}"`

- 빠른 모드로 라벨, 프로젝트 및 기한이 있는 높은 우선순위 작업 추가:

`todoist quick '#{{프로젝트_이름}} "{{tmr 9am}}" p{{1}} {{작업_이름}} @{{라벨_이름}}'`

- 헤더 및 색상이 있는 모든 작업 나열:

`todoist --header --color list`

- 높은 우선순위의 모든 작업 나열:

`todoist list --filter p{{1}}`

- 지정된 라벨이 있는 오늘의 높은 우선순위 작업 나열:

`todoist list --filter '(@{{라벨_이름}} | {{today}}) & p{{1}}'`

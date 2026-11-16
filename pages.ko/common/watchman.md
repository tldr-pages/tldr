# watchman

> 파일을 감시하고 변경 사항이 발생할 때 작업을 트리거하는 서비스.
> 더 많은 정보: <https://facebook.github.io/watchman/docs/cli-options>.

- 지정된 디렉터리를 포함하는 프로젝트의 루트 디렉터리를 유추하고, 파일 및 하위 폴더의 변경 사항을 감시:

`watchman watch-project {{경로/대상/디렉터리}}`

- 감시 중인 디렉터리에서 지정된 파일명 패턴의 파일이 변경될 때 명령을 실행하는 트리거 추가:

`watchman -- trigger {{경로/대상/감시_디렉터리}} {{트리거_이름}} '{{패턴}}' -- {{명령어}}`

- 감시 중인 모든 디렉터리 나열:

`watchman watch-list`

- 디렉터리에 대한 감시 및 관련 트리거 삭제:

`watchman watch-del {{경로/대상/감시_디렉터리}}`

- 감시 중인 모든 디렉터리 및 트리거 삭제:

`watchman watch-del-all`

- 감시 중인 디렉터리의 모든 트리거 나열:

`watchman trigger-list {{경로/대상/감시_디렉터리}}`

- 감시 중인 디렉터리에서 트리거 삭제:

`watchman trigger-del {{경로/대상/감시_디렉터리}} {{트리거_이름}}`

- 다음에 `watchman` 명령을 호출할 때까지 `watchman` 일시 중지:

`watchman shutdown-server`

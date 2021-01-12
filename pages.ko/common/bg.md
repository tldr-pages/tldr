# bg

> 일시 중단된 작업을 다시 시작하고 (예. `Ctrl + Z`), 그 작업이 background에서 동작하게 유지.

- 가장 최근에 일시 중단된 작업을 재개하고 background에서 실행:

`bg`

- 특정 작업을 재개하고(`jobs -l` 를 사용하여 ID 가져오기) background에서 실행:

`bg %{{job_id}}`

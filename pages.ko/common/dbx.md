# dbx

> Databricks 플랫폼과 상호작용.
> 참고: 이 도구는 더 이상 사용되지 않으며, Databricks Asset Bundles 사용이 권장됨.
> 더 많은 정보: <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>.

- 현재 작업 디렉터리에 새로운 `dbx` 프로젝트를 생성:

`dbx configure --profile {{DEFAULT}}`

- 지정한 경로의 로컬 파일을 DBFS로 동기화하고 변경 사항을 감시:

`dbx sync dbfs --source {{경로/대상/디렉터리}} --dest {{경로/대상/원격_디렉터리}}`

- 지정한 워크플로를 아티팩트 스토리지에 배포:

`dbx deploy {{워크플로우_이름}}`

- 지정한 워크플로를 배포한 후 실행:

`dbx launch {{워크플로우_이름}}`

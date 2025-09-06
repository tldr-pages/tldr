# argocd app

> Argo CD로 애플리케이션을 관리하는 명령줄 인터페이스.
> 더 많은 정보: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- 애플리케이션 목록 보여주기:

`argocd app list --output {{json|yaml|wide}}`

- 애플리케이션 세부사항 가져오기:

`argocd app get {{애플리케이션_이름}} --output {{json|yaml|wide}}`

- 애플리케이션을 내부적으로 (Argo CD가 실행되고 있는 동일한 클러스터에) 배포:

`argocd app create {{애플리케이션_이름}} --repo {{git_레포지토리_주소}} --path {{경로/대상/레포지토리}} --dest-server https://kubernetes.default.svc --dest-namespace {{네임스페이스}}`

- 애플리케이션 삭제:

`argocd app delete {{애플리케이션_이름}}`

- 애플리케이션 자동 동기화 활성화:

`argocd app set {{애플리케이션_이름}} --sync-policy auto --auto-prune --self-heal`

- 클러스터에 영향을 주지 않고 애플리케이션 동기화 미리보기:

`argocd app sync {{애플리케이션_이름}} --dry-run --prune`

- 애플리케이션 배포 기록 표시:

`argocd app history {{애플리케이션_이름}} --output {{wide|id}}`

- 히스토리 ID를 기준으로 이전 배포 버전으로 애플리케이션 롤백 (예상치 못한 리소스 삭제):

`argocd app rollback {{애플리케이션_이름}} {{히스토리_id}} --prune`

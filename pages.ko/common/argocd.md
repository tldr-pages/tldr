# argocd

> Argo CD 서버를 제어하는 명령줄 인터페이스.
> `argocd app`과 같은 일부 하위 명령에는 자체 사용 문서가 있습니다.
> 더 많은 정보: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Argo CD 서버에 로그인:

`argocd login --insecure --username {{사용자}} --password {{비밀번호}} {{argocd_서버:포트}}`

- 애플리케이션 목록 보여주기:

`argocd app list`

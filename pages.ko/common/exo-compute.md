# exo compute

> Exoscale Compute 리소스를 관리하는 CLI 명령어.
> `instance`와 같은 일부 하위 명령어는 별도의 문서를 가집니다.
> 더 많은 정보: <https://community.exoscale.com/product/>.

- Exoscale Compute 리소스 (예: 인스턴스, 보안 그룹, SKS 클러스터 등) 빠르게 생성:

`exo compute {{리소스_타입}} create {{리소스_이름}}`

- Exoscale Compute 인스턴스 타입 목록 조회:

`exo compute instance-type list`

- Compute 인스턴스 접속용 SSH 키 등록:

`exo compute ssh-key register {{키_이름}} {{공개_키_파일}}`

- SSH 키를 포함하여 Compute 인스턴스 생성:

`exo compute instance create {{인스턴스_이름}} {{ssh_키_이름}}`

- 특정 Compute 인스턴스 스냅샷을 기반으로 새로운 Compute 인스턴스 등록 (Compute 인스턴스를 빠르게 복제하고 싶을 때 유용):

`exo compute instance template register {{템플릿_이름}} --from-snapshot {{스냅샷_아이디}}`

- 기존 보안 그룹에 새로운 규칙 추가:

`exo compute security-group rule add {{보안_그룹_이름_또는_아이디}} --description '{{Allow SSH access}}' --flow {{ingress}} --port {{22}} --network {{0.0.0.0/0}}`

- 네트워크 로그 밸런서의 서비스 관리:

`exo compute load-balancer service add {{load_balancer_이름_또는_아이디}} {{서비스_이름}} --port {{서비스_포트}}`

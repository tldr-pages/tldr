# nova

> 컴퓨팅 인스턴스를 프로비저닝하는 방법을 제공하는 OpenStack 프로젝트.
> 더 많은 정보: <https://docs.openstack.org/nova/latest/>.

- 현재 테넌트의 VM 나열:

`nova list`

- 모든 테넌트의 VM 나열 (관리자 사용자만 가능):

`nova list --all-tenants`

- 특정 호스트에 VM 부팅:

`nova boot --nic net-id={{네트워크_ID}} --image {{이미지_ID}} --flavor {{플레이버}} --availability-zone nova:{{호스트_이름}} {{VM_이름}}`

- 서버 시작:

`nova start {{서버}}`

- 서버 중지:

`nova stop {{서버}}`

- 특정 VM에 네트워크 인터페이스 연결:

`nova interface-attach --net-id {{네트워크_ID}} {{서버}}`

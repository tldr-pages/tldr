# kubetail

> 여러 Kubernetes 포드의 로그를 동시에 추적하는 유틸리티.
> 더 많은 정보: <https://github.com/johanhaleby/kubetail>.

- 여러 포드의 로그를 한 번에 추적 (포드 이름이 "my_app"으로 시작하는 경우):

`kubetail {{my_app}}`

- 여러 포드에서 특정 컨테이너의 로그만 추적:

`kubetail {{my_app}} -c {{my_container}}`

- 여러 포드에서 여러 컨테이너의 로그를 추적:

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- 여러 애플리케이션의 로그를 동시에 추적하려면 쉼표로 구분:

`kubetail {{my_app_1}},{{my_app_2}}`

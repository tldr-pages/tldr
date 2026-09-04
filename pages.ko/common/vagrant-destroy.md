# vagrant destroy

> 게스트 머신을 중지하고 관련된 모든 리소스를 삭제.
> 설치된 box는 그대로 유지됨.
> 관련 항목: `vagrant`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/destroy>.

- 현재 실행 중인 machine 삭제:

`vagrant destroy`

- 이름 또는 ID를 지정하여 machine 삭제:

`vagrant destroy {{이름|id}}`

- 확인 없이 machine 강제 삭제:

`vagrant destroy {{[-f|--force]}}`

- machine을 강제 종료하지 않고 정상 종료 후 삭제(gracefully):

`vagrant destroy {{[-g|--graceful]}}`

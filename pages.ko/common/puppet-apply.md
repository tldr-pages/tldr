# puppet apply

> Puppet 매니페스트를 로컬에서 적용.
> 더 많은 정보: <https://github.com/puppetlabs/puppet/blob/main/references/man/apply.md>.

- 매니페스트 적용:

`puppet apply {{경로/대상/매니페스트}}`

- Puppet 코드 실행:

`puppet apply --execute {{코드}}`

- 특정 모듈 및 Hiera 구성 파일 사용:

`puppet apply --modulepath {{경로/대상/폴더}} --hiera_config {{경로/대상/파일}} {{경로/대상/매니페스트}}`

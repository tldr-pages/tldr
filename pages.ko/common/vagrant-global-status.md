# vagrant global-status

> 시스템에 있는 모든 Vagrant machine의 상태를 표시.
> 정보는 캐시를 기반으로 하므로 오래된 항목이 남을 수 있어, 이러한 경우에 정리가 필요.
> 관련 항목: `vagrant`, `vagrant status`.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/global-status>.

- 모든 machine의 상태 표시:

`vagrant global-status`

- 오래된 캐시 항목을 정리하여 결과에서 제거:

`vagrant global-status --prune`

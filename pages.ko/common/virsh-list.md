# virsh-list

> 가상 머신의 ID, 이름, 상태 나열.
> 같이 보기: `virsh`.
> 더 많은 정보: <https://manned.org/virsh>.

- 실행 중인 가상 머신에 대한 정보 나열:

`virsh list`

- 상태에 관계없이 가상 머신에 대한 정보 나열:

`virsh list --all`

- 자동 시작이 활성화되거나 비활성화된 가상 머신에 대한 정보 나열:

`virsh list --all --{{autostart|no-autostart}}`

- 스냅샷 유무에 관계없이 가상 머신에 대한 정보 나열:

`virsh list --all --{{with-snapshot|without-snapshot}}`

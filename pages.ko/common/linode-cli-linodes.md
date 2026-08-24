# linode-cli linodes

> Linode 인스턴스를 관리.
> 관련 항목: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- 모든 Linode 나열:

`linode-cli linodes list`

- 새 Linode 생성:

`linode-cli linodes create --type {{linode_유형}} --region {{지역}} --image {{이미지_id}}`

- 특정 Linode의 세부 정보 보기:

`linode-cli linodes view {{linode_id}}`

- Linode 설정 업데이트:

`linode-cli linodes update {{linode_id}} --label {{새_레이블}}`

- Linode 삭제:

`linode-cli linodes delete {{linode_id}}`

- Linode에 전원 관리 작업 수행:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- Linode에 대한 사용 가능한 백업 목록:

`linode-cli linodes backups-list {{linode_id}}`

- Linode에 백업 복원:

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{백업_id}}`

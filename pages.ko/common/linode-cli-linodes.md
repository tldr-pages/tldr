# linode-cli linodes

> Linode 인스턴스를 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>.

- 모든 Linode 나열:

`linode-cli linodes list`

- 새 Linode 생성:

`linode-cli linodes create --type {{linode_유형}} --region {{지역}} --image {{이미지_ID}}`

- 특정 Linode의 세부 정보 보기:

`linode-cli linodes view {{linode_ID}}`

- Linode 설정 업데이트:

`linode-cli linodes update {{linode_ID}} --label {{새_레이블}}`

- Linode 삭제:

`linode-cli linodes delete {{linode_ID}}`

- Linode에 전원 관리 작업 수행:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_ID}}`

- Linode에 대한 사용 가능한 백업 목록:

`linode-cli linodes backups-list {{linode_ID}}`

- Linode에 백업 복원:

`linode-cli linodes backups-restore {{linode_ID}} --backup-id {{백업_ID}}`

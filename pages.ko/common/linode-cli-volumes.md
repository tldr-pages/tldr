# linode-cli volumes

> Linode 볼륨 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>.

- 현재 볼륨 나열:

`linode-cli volumes list`

- 새 볼륨 생성 및 특정 Linode에 연결:

`linode-cli volumes create --label {{볼륨_레이블}} --size {{크기_GB}} --linode-id {{linode_id}}`

- 특정 Linode에 볼륨 연결:

`linode-cli volumes attach {{볼륨_id}} --linode-id {{linode_id}}`

- Linode에서 볼륨 분리:

`linode-cli volumes detach {{볼륨_id}}`

- 볼륨 크기 조정 (참고: 크기만 증가 가능):

`linode-cli volumes resize {{볼륨_id}} --size {{새_크기_GB}}`

- 볼륨 삭제:

`linode-cli volumes delete {{볼륨_id}}`

# linode-cli tickets

> Linode 지원 티켓 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>.

- 지원 티켓 목록 보기:

`linode-cli tickets list`

- 새 티켓 열기:

`linode-cli tickets create --summary "{{티켓에 대한 요약 또는 간단한 제목}}" --description "{{문제에 대한 자세한 설명}}"`

- 티켓에 대한 답변 목록 보기:

`linode-cli tickets replies {{티켓_ID}}`

- 특정 티켓에 답장하기:

`linode-cli tickets reply {{티켓_ID}} --description "{{답변 내용}}"`

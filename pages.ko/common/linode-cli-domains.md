# linode-cli domains

> Linode 도메인 및 DNS 구성 관리.
> 같이 보기: `linode-cli`.
> 더 많은 정보: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>.

- 관리되는 모든 도메인 나열:

`linode-cli domains list`

- 새 관리 도메인 생성:

`linode-cli domains create --domain {{도메인_이름}} --type {{master|slave}} --soa-email {{이메일}}`

- 특정 도메인의 세부 정보 보기:

`linode-cli domains view {{도메인_ID}}`

- 관리 도메인 삭제:

`linode-cli domains delete {{도메인_ID}}`

- 특정 도메인의 레코드 나열:

`linode-cli domains records-list {{도메인_ID}}`

- 도메인에 DNS 레코드 추가:

`linode-cli domains records-create {{도메인_ID}} --type {{A|AAAA|CNAME|MX|...}} --name {{서브도메인}} --target {{대상_값}}`

- 도메인의 DNS 레코드 업데이트:

`linode-cli domains records-update {{도메인_ID}} {{레코드_ID}} --target {{새로운_대상_값}}`

- 도메인에서 DNS 레코드 삭제:

`linode-cli domains records-delete {{도메인_ID}} {{레코드_ID}}`

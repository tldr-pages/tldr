# az sshkey

> 가상 머신으로 SSH 공개 키를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/sshkey>.

- 새로운 SSH 키를 생성:

`az sshkey create --name {{이름}} --resource-group {{리소스_그룹}}`

- 기존 SSH 키 업로드:

`az sshkey create --name {{이름}} --resource-group {{리소스_그룹}} --public-key "{{@path/to/key.pub}}"`

- 모든 SSH 공개 키를 나열:

`az sshkey list`

- SSH 공개 키를 대한 정보 표시:

`az sshkey show --name {{이름}} --resource-group {{리소스_그룹}}`

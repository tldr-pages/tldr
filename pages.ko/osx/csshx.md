# csshX

> macOS용 클러스터 SSH 도구.
> 더 많은 정보: <https://github.com/brockgr/csshx>.

- 여러 호스트에 연결:

`csshX {{호스트명1}} {{호스트명2}}`

- 지정된 SSH 키를 사용하여 여러 호스트에 연결:

`csshX {{사용자@호스트명1}} {{사용자@호스트명2}} --ssh_args "-i {{경로/대상/키_파일.pem}}"`

- `/etc/clusters`에 정의된 클러스터에 연결:

`csshX cluster1`

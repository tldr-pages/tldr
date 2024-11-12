# choco apikey

> Chocolatey 소스의 API 키 관리.
> 더 많은 정보: <https://chocolatey.org/docs/commands-apikey>.

- 소스 및 해당 API 키 목록 표시:

`choco apikey`

- 특정 소스 및 해당 API 키 표시:

`choco apikey --source "{{소스_URL}}"`

- 소스에 대한 API 키 설정:

`choco apikey --source "{{소스_URL}}" --key "{{API_키}}"`

- 소스에 대한 API 키 제거:

`choco apikey --source "{{소스_URL}}" --remove`

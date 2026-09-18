# pfctl

> 패킷 필터 장치를 제어.
> 더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?query=pfctl>.

- 패킷 필터 활성화:

`sudo pfctl -e`

- 패킷 필터 비활성화:

`sudo pfctl -d`

- 설정 파일에서 규칙 불러오기:

`sudo pfctl -f {{경로/대상/pf.conf}}`

- 현재 활성화된 모든 규칙 표시:

`pfctl -sr`

- 패킷 필터 상태 정보 표시:

`pfctl -s info`

- 모든 규칙을 초기화:

`sudo pfctl -F rules`

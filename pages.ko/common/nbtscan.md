# nbtscan

> 네트워크를 스캔하여 NetBIOS 이름 정보를 검색.
> 더 많은 정보: <https://github.com/resurrecting-open-source-projects/nbtscan>.

- 네트워크에서 NetBIOS 이름 스캔:

`nbtscan {{192.168.0.1/24}}`

- 단일 IP 주소 스캔:

`nbtscan {{192.168.0.1}}`

- 자세한 출력 표시:

`nbtscan -v {{192.168.0.1/24}}`

- `/etc/hosts` 형식으로 출력 표시:

`nbtscan -e {{192.168.0.1/24}}`

- 스캔할 IP 주소/네트워크를 파일에서 읽기:

`nbtscan -f {{경로/대상/파일.txt}}`

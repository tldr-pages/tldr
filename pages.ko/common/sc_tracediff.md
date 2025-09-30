# sc_tracediff

> 경로가 변경된 traceroute 경로를 표시.
> 더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 두 `warts` 파일에서 traceroute의 차이점 표시:

`sc_tracediff {{경로/대상/파일1.warts}} {{경로/대상/파일2.warts}}`

- 두 `warts` 파일에서 변경되지 않은 traceroute도 포함하여 차이점 표시:

`sc_tracediff -a {{경로/대상/파일1.warts}} {{경로/대상/파일2.warts}}`

- 두 `warts` 파일에서 traceroute의 차이점을 표시하고 가능하면 IP 주소 대신 DNS 이름을 표시:

`sc_tracediff -n {{경로/대상/파일1.warts}} {{경로/대상/파일2.warts}}`

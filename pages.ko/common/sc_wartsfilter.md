# sc_wartsfilter

> `warts` 파일에서 특정 레코드를 선택.
> 더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 특정 목적지를 가진 모든 데이터 레코드를 필터링하여 별도의 파일로 저장:

`sc_wartsfilter -i {{경로/대상/입력.warts}} -o {{경로/대상/출력.warts}} -a {{192.0.2.5}} -a {{192.0.2.6}}`

- 특정 접두사를 가진 목적지의 모든 레코드를 필터링하여 별도의 파일로 저장:

`sc_wartsfilter -i {{경로/대상/입력.warts}} -o {{경로/대상/출력.warts}} -a {{2001:db8::/32}}`

- 특정 작업을 사용한 모든 레코드를 필터링하여 JSON으로 출력:

`sc_wartsfilter -i {{경로/대상/입력.warts}} -t {{ping}} | sc_warts2json`

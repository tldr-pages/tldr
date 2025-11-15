# sc_warts2pcap

> `warts` 객체에 포함된 패킷을 PCAP 파일로 작성.
> 이는 tbit, sting 및 sniff에 대해서만 가능합니다.
> 더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 여러 `warts` 파일의 데이터를 하나의 PCAP 파일로 변환:

`sc_warts2pcap -o {{경로/대상/출력.pcap}} {{경로/대상/파일1.warts 경로/대상/파일2.warts ...}}`

- `warts` 파일의 데이터를 PCAP 파일로 변환하고 패킷을 타임스탬프별로 정렬:

`sc_warts2pcap -s -o {{경로/대상/출력.pcap}} {{경로/대상/파일.warts}}`

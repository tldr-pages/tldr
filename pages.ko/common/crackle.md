# crackle

> BLE(Bluetooth Low Energy) 암호화를 크랙하고 해독.
> 더 많은 정보: <https://github.com/mikeryan/crackle>.

- 녹음된 BLE 통신에 임시 키(TK)를 복구하는 데 필요한 패킷이 포함되어 있는지 확인:

`crackle -i {{경로/대상/입력.pcap}}`

- 무차별 대입을 사용해 기록된 페어링 이벤트의 TK를 복구하고 이를 사용하여 모든 후속 통신을 해독:

`crackle -i {{경로/대상/입력.pcap}} -o {{경로/대상/복호화데이터.pcap}}`

- 지정된 장기 키 (LTK)를 사용하여 녹음된 통신을 해독:

`crackle -i {{경로/대상/입력.pcap}} -o {{경로/대상/복호화데이터.pcap}} -l {{81b06facd90fe7a6e9bbd9cee59736a7}}`

# openvpn

> OpenVPN 클라이언트 및 데몬 바이너리.
> 더 많은 정보: <https://openvpn.net/community-docs/community-articles/openvpn-2-6-manual.html>.

- 구성 파일을 사용하여 서버에 연결:

`sudo openvpn {{경로/대상/클라이언트.conf}}`

- bob.example.com 호스트에서 안전하지 않은 피어-투-피어 터널 설정 시도:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}}`

- 암호화 없이 대기 중인 bob.example.com 호스트에 연결:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}}`

- 암호화 키를 생성하고 파일에 저장:

`openvpn --genkey secret {{경로/대상/키}}`

- 고정 키를 사용하여 bob.example.com 호스트에서 피어-투-피어 터널 설정 시도:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}} --secret {{경로/대상/키}}`

- bob.example.com에서 사용된 동일한 고정 키로 대기 중인 bob.example.com 호스트에 연결:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}} --secret {{경로/대상/키}}`

# wol

> Wake-on-LAN 매직 패킷을 보내는 클라이언트.
> 더 많은 정보: <https://sourceforge.net/projects/wake-on-lan/>.

- 장치에 WoL 패킷 전송:

`wol {{MAC_주소}}`

- 다른 서브넷의 IP를 기반으로 장치에 WoL 패킷 전송:

`wol --ipaddr={{IP_주소}} {{MAC_주소}}`

- 다른 서브넷의 호스트명을 기반으로 장치에 WoL 패킷 전송:

`wol --host={{호스트명}} {{MAC_주소}}`

- 특정 포트의 호스트에 WoL 패킷 전송:

`wol --port={{포트_번호}} {{MAC_주소}}`

- [하]드웨어 주소, IP 주소/호스트명, 선택적 포트 및 SecureON 비밀번호를 [f]파일에서 읽기:

`wol --file={{경로/대상/파일}}`

- [v]자세히 출력 켜기:

`wol {{[-v|--verbose]}} {{MAC_주소}}`

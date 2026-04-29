# IPXNET

> 멀티 플레이 게임을 위해 IPX 네트워킹을 에뮬레이션하는 도구(클라이언트-서버 모델).
> 더 많은 정보: <https://www.dosbox.com/wiki/Connectivity>.

- IPX 서버 시작 (기본 UDP 포트 213):

`IPXNET startserver`

- 특정 포트로 서버 시작:

`IPXNET startserver {{19900}}`

- 서버 IP로 클라이언트 연결:

`IPXNET connect {{192.168.2.100}}`

- 특정 포트로 클라이언트 연결:

`IPXNET connect {{192.168.2.100}} {{19900}}`

- 네트워크 상태 확인:

`IPXNET status`

- 속도 및 클라이언트 테스트를 위한 ping:

`IPXNET ping`

- 클라이언트 연결 해제:

`IPXNET disconnect`

- 서버 종료 (모든 클라이언트 연결 해제 후):

`IPXNET stopserver`

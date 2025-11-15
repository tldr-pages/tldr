# nxc vnc

> VNC 서버를 펜테스트하고 익스플로잇합니다.
> 더 많은 정보: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- 지정된 [u]사용자명 및 [p]비밀번호 목록의 모든 조합을 시도하여 유효한 자격 증명 검색:

`nxc vnc {{192.168.178.2}} -u {{경로/대상/사용자명목록.txt}} -p {{경로/대상/비밀번호목록.txt}}`

- VNC-sleep을 통해 속도 제한 회피:

`nxc vnc {{192.168.178.2}} -u {{경로/대상/사용자명목록.txt}} -p {{경로/대상/비밀번호목록.txt}} --vnc-sleep {{10}}`

- 지정된 시간만큼 대기한 후 원격 시스템에서 스크린샷 촬영:

`nxc vnc {{192.168.178.2}} -u {{사용자명}} -p {{비밀번호}} --screenshot --screentime {{10}}`

# zoneadm

> Oracle Solaris zones를 관리하는 도구.
> 더 많은 정보: <https://docs.oracle.com/cd/E88353_01/html/E72487/zoneadm-8.html>.

- 모든 zone과 상태 목록 출력:

`zoneadm list -cv`

- 특정 zone 설정 검증:

`sudo zoneadm -z {{zone_이름}} verify`

- zone 설치:

`sudo zoneadm -z {{zone_이름}} install`

- zone 시작:

`sudo zoneadm -z {{zone_이름}} boot`

- zone 재시작:

`sudo zoneadm -z {{zone_이름}} reboot`

- zone 내부 종료 스크립트 무시하는 zone 강제 중지:

`sudo zoneadm -z {{zone_이름}} halt`

- zone 제거:

`sudo zoneadm -z {{zone_이름}} uninstall`

# synopkg

> Synology DiskStation Manager의 패키지 관리 도구.
> 더 많은 정보: <https://www.synology.com/dsm>.

- 설치된 패키지의 이름 나열:

`synopkg list --name`

- 특정 패키지에 의존하는 패키지 나열:

`synopkg list --depend-on {{패키지}}`

- 패키지 시작/중지:

`sudo synopkg {{start|stop}} {{패키지}}`

- 패키지 상태 출력:

`synopkg status {{패키지}}`

- 패키지 제거:

`sudo synopkg uninstall {{패키지}}`

- 패키지 업데이트 가능 여부 확인:

`synopkg checkupdate {{패키지}}`

- 모든 패키지를 최신 버전으로 업그레이드:

`sudo synopkg upgradeall`

- synopkg 파일에서 패키지 설치:

`sudo synopkg install {{경로/대상/패키지.spk}}`

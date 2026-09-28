# xlsclients

> X11 디스플레이에서 실행 중인 클라이언트 애플리케이션 목록을 표시.
> 더 많은 정보: <https://manned.org/xlsclients>.

- 기본 디스플레이의 클라이언트 목록 표시:

`xlsclients`

- 모든 화면의 클라이언트 목록 표시:

`xlsclients -a`

- 클라이언트의 상세 정보 표시:

`xlsclients -l`

- 클라이언트별 명령 출력 길이를 지정한 문자 수를 제한:

`xlsclients -m {{최대_명령어_길이}}`

- 확인할 디스플레이 지정:

`xlsclients -display :{{전시_번호}}`

- 원격 호스트의 디스플레이에서 실행 중인 클라이언트 목록 표시:

`xlsclients -display {{원격_호스트}}:0`

- 버전 정보 표시:

`xlsclients -version`

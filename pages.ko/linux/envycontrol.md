# envycontrol

> Nvidia Optimus 노트북을 위한 GPU 전환 도구.
> 더 많은 정보: <https://github.com/bayasdev/envycontrol#%EF%B8%8F-usage>.

- 다른 GPU 모드로 전환:

`sudo envycontrol -s {{nvidia|integrated|hybrid}}`

- 디스플레이 관리자 수동 지정:

`envycontrol --dm`

- 현재 GPU 모드 확인:

`sudo envycontrol --query`

- 설정 초기화:

`sudo envycontrol --reset`

- 도움말 표시:

`envycontrol --help`

- 버전 표시:

`envycontrol --version`

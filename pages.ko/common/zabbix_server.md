# zabbix_server

> Zabbix 소프트웨어의 핵심 데몬.
> 더 많은 정보: <https://manned.org/zabbix_server>.

- 기본 설정 파일을 사용해 서버를 시작:

`zabbix_server`

- 사용자 지정 설정 파일을 사용하여 서버 시작:

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}}`

- 서버를 포그라운드에서 실행:

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}} {{[-f|--foreground]}}`

- 설정 파일을 테스트하고 종료:

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}} {{[-T|--test-config]}}`

- 설정 캐시 다시 불러오기 (런타임 제어):

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}} {{[-R|--runtime-control]}} config_cache_reload`

- housekeeper 실행 (런타임 제어):

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}} {{[-R|--runtime-control]}} housekeeper_execute`

- 모든 프로세스의 로그 수준 높이기 또는 낮추기 (런타임 제어):

`zabbix_server {{[-c|--config]}} {{경로/대상/zabbix_서버.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- 도움말 표시:

`zabbix_server {{[-h|--help]}}`

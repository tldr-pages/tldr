# openocd

> OpenOCD를 사용하여 임베디드 시스템을 디버깅 및 프로그래밍하는 도구.
> 더 많은 정보: <https://manned.org/openocd>.

- 설정 파일을 사용해 보드에 OpenOCD 세션 연결:

`openocd {{[-f|--file]}} {{구성_파일.cfg}}`

- 여러 설정 파일을 사용하여 보드에 OpenOCD 세션 연결 :

`openocd {{[-f|--file]}} {{config_file1.cfg}} {{[-f|--file]}} {{config_file2.cfg}}`

- 22설정 파일 및 서버 시작 시 실행할 명령을 함께 지정하여 보드에 OpenOCD 세션 연결:

`openocd {{[-f|--file]}} {{config_file.cfg}} {{[-c|--command]}} "{{command}}"`

- 지정한 경로의 설정 파일 경로를 사용:

`openocd {{[-s|--search]}} {{path/to/search}} {{[-f|--file]}} {{config_file.cfg}}`

- [대화형] OpenOCD 시작 후, GDB를 기본 포트(3333)로 연결:

`target extended-remote localhost`

- 사이트 전역 스크립트 라이브러리 목록 출력:

`ls /usr/local/share/openocd/scripts`

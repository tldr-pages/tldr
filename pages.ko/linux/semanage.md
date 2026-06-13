# semanage

> SELinux 영구 정책 관리 도구.
> `boolean`, `fcontext`, `port` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://manned.org/semanage>.

- SELinux 불리언 설정 또는 해제. 불리언은 관리자가 정책 규칙이 제한된 프로세스 유형(도메인)에 어떻게 영향을 미치는지 사용자 정의할 수 있게 함:

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`

- 사용자 정의 파일 컨텍스트 레이블링 규칙 추가. 파일 컨텍스트는 제한된 도메인이 접근할 수 있는 파일을 정의함:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '/mnt/share(/.*)?'`

- 사용자 정의 포트 레이블링 규칙 추가. 포트 레이블은 제한된 도메인이 청취할 수 있는 포트를 정의함:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- 제한된 도메인에 대한 허용 모드 설정 또는 해제. 도메인별 허용 모드는 `setenforce`에 비해 더 세분화된 제어를 제공함:

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`

- 기본 저장소에서 로컬 사용자 정의 출력:

`sudo semanage export {{[-f|--output_file]}} {{경로/대상/파일}}`

- `semanage export`로 생성된 파일을 로컬 사용자 정의에 가져오기 (주의: 현재 사용자 정의가 제거될 수 있음!):

`sudo semanage import {{[-f|--input_file]}} {{경로/대상/파일}}`

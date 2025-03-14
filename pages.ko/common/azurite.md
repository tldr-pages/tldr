# azurite

> 로컬 환경의 Azure Storage API 호환 서버 (에뮬레이터).
> 더 많은 정보: <https://www.npmjs.com/package/azurite>.

- 기존 위치를 작업공간 경로로 사용:

`azurite {{[-l|--location]}} {{경로/대상/디렉터리}}`

- 콘솔에 표시된 액세스 로그를 비활성화:

`azurite {{[-s|--silent]}}`

- 파일 경로를 로그 대상으로 제공하여, 디버그 로그를 활성화:

`azurite {{[-d|--debug]}} {{경로/대상/debug.log}}`

- Blob/Queue/Table 서비스의 수신 주소를 사용자 정의:

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- Blob/Queue/Table 서비스의 수신 포트를 사용자 정의:

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`

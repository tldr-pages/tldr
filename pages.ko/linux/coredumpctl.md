# coredumpctl

> 저장된 코어 덤프와 메타데이터를 검색하고 처리합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- 캡처된 모든 코어 덤프 나열:

`coredumpctl list`

- 특정 프로그램의 캡처된 코어 덤프 나열:

`coredumpctl list {{프로그램}}`

- `PID`와 일치하는 프로그램의 코어 덤프 정보 표시:

`coredumpctl info {{PID}}`

- 특정 프로그램의 마지막 코어 덤프를 사용하여 디버거 호출:

`coredumpctl debug {{프로그램}}`

- 특정 프로그램의 마지막 코어 덤프를 파일로 추출:

`coredumpctl --output {{경로/대상/파일}} dump {{프로그램}}`

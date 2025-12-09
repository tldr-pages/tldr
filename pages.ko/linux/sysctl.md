# sysctl

> 커널 런타임 변수를 나열하고 변경합니다.
> 더 많은 정보: <https://manned.org/sysctl.8>.

- 사용 가능한 모든 변수와 그 값을 표시:

`sysctl -a`

- 변경 가능한 커널 상태 변수를 설정:

`sysctl -w {{섹션.조정가능}}={{값}}`

- 현재 열려 있는 파일 핸들러 수를 확인:

`sysctl fs.file-nr`

- 동시에 열 수 있는 파일의 제한을 확인:

`sysctl fs.file-max`

- `/etc/sysctl.conf` 파일의 변경 사항을 적용:

`sysctl -p`

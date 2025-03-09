# stty

> 터미널 장치 인터페이스의 옵션 설정.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- 현재 터미널의 모든 설정 표시:

`stty --all`

- 행 또는 열의 수 설정:

`stty {{rows|cols}} {{수}}`

- 장치의 실제 전송 속도 확인:

`stty --file {{경로/대상/장치_파일}} speed`

- 현재 터미널의 모든 모드를 적절한 값으로 재설정:

`stty sane`

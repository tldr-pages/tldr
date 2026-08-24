# stty

> 터미널 장치 인터페이스의 옵션을 설정하거자 조회.
> 관련 항목: `tput`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- 현재 터미널 크기를 표시:

`stty size`

- 현재 터미널의 모든 설정을 표시:

`stty {{[-a|--all]}}`

- 행 또는 열의 개수를 설정:

`stty {{rows|cols}} {{개수}}`

- 장치의 실제 전송 속도를 확인:

`stty {{[-F|--file]}} {{경로/대상/장치_파일}} speed`

- 현재 터미널에 대해 모든 모드를 적절한 기본값으로 재설정:

`stty sane`

- Switch between raw and normal mode:

`stty {{raw|cooked}}`

- Turn character echoing off or on:

`stty {{-echo|echo}}`

- 도움말 표시:

`stty --help`

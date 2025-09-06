# run-mailcap

> MailCap 프로그램 실행.
> mailcap 파일(또는 그 별칭)의 항목을 통해 프로그램을 실행하여 각 MIME 타입/파일을 주어진 작업으로 처리.
> 더 많은 정보: <https://manned.org/run-mailcap>.

- run-mailcap에서 작업 플래그를 사용하여 개별 작업/프로그램 실행:

`run-mailcap --action=ACTION [--option[=value]]`

- 간단한 사용법:

`run-mailcap --action=ACTION {{파일명}}`

- 추가 정보를 켜기:

`run-mailcap --action=ACTION --debug {{파일명}}`

- "copiousoutput" 지시문을 무시하고 출력을 `stdout`으로 전달:

`run-mailcap --action=ACTION --nopager {{파일명}}`

- 실제로 실행하지 않고 발견된 명령을 표시:

`run-mailcap --action=ACTION --norun {{파일명}}`

# cupsd

> CUPS 인쇄 서버용 서버 데몬.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- 백그라운드에서 `cupsd`를 데몬으로 시작:

`cupsd`

- 포어그라운드에서 `cupsd`를 시작:

`cupsd -f`

- 필요에 따라 `cupsd` 실행([l]aunch) (일반적으로 `launchd` 또는 `systemd`에서 사용됨):

`cupsd -l`

- Start `cupsd` using the specified [`c`]`upsd.conf` configuration file:

`cupsd -c {{경로/대상/cupsd.conf}}`

- 지정된 `cups-file`[`s`]`.conf` 구성 파일을 사용하여 `cupsd`를 시작:

`cupsd -s {{경로/대상/cups-파일.conf}}`

- [`c`]`upsd.conf` 구성 파일에 오류가 있는지 확인([t]est):

`cupsd -t -c {{path/to/cupsd.conf}}`

- `cups-file`[`s`]`.conf` 구성 파일들에 오류가 있는지 확인([t]est):

`cupsd -t -s {{경로/대상/cups-파일.conf}}`

- 도움말 표시:

`cupsd -h`

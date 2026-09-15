# fwupdtool

> 장치의 firmware를 수동으로 업데이트하거나 firmware 파일을 관리.
> 관련 항목: `fwupdmgr`.
> 더 많은 정보: <https://github.com/fwupd/fwupd/blob/main/src/fwupdtool.md>.

- `fwupd`가 감지한 모든 장치 표시:

`fwupdtool get-devices`

- 파일에서 firmware 설치:

`fwupdtool install {{경로/대상/firmware}}`

- 도움말 표시:

`fwupdtool {{[-h|--help]}}`

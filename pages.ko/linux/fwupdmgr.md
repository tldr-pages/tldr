# fwupdmgr

> `fwupd`를 사용하여 UEFI를 포함한 장치 펌웨어 업데이트.
> 더 많은 정보: <https://github.com/fwupd/fwupd/blob/main/src/fwupdmgr.md>.

- fwupd에 의해 감지된 모든 장치 표시:

`fwupdmgr get-devices`

- LVFS에서 최신 펌웨어 메타데이터 다운로드:

`fwupdmgr refresh`

- 시스템의 장치에 사용할 수 있는 업데이트 나열:

`fwupdmgr get-updates`

- 펌웨어 업데이트 설치:

`fwupdmgr update`

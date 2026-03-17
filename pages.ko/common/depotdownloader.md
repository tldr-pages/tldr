# depotdownloader

> Steam 콘텐츠/디포(depot)를 다운로드.
> 더 많은 정보: <https://github.com/SteamRE/DepotDownloader>.

- 애플리케이션 다운로드:

`depotdownloader -app {{108600}}`

- 특정 디포(depot)를 지정한 디렉터리에 다운로드:

`depotdownloader -app {{108600}} -depot {{108603}} -dir {{경로/대상/디렉터리}}`

- Steam 계정을 사용해 다운로드:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}"`

- 디포(depot)를 다운로드하고 이후 다운로드를 위해 비밀번호를 저장:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}" -remember-password`

- 특정 디포(depot) 매니페스트를 다운로드:

`depotdownloader -app {{346110}} -depot {{346111}} -manifest {{6154025194991279746}}`

- 특정 브랜치에서 다운로드:

`depotdownloader -app {{108600}} -depot {{108603}} -branch "{{unstable}}"`

- 콘텐츠를 제외하고 내부 매니페스트만 다운로드:

`depotdownloader -app {{108600}} -depot {{108603}} -manifest-only`

- pubfile/workshop ID를 사용해 workshop 콘텐츠를 다운로드:

`depotdownloader -app {{108600}} -pubfile {{2503622437}}`

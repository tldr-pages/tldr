# xcodes runtimes

> Xcode 시뮬레이터 런타임 관리.
> 더 많은 정보: <https://github.com/xcodesorg/xcodes#commands>.

- 사용 가능한 모든 시뮬레이터 런타임 표시:

`xcodes runtimes --include-betas`

- 시뮬레이터 런타임 다운로드:

`xcodes runtimes download {{런타임_이름}}`

- 시뮬레이터 런타임 다운로드 및 설치:

`xcodes runtimes install {{런타임_이름}}`

- 특정 iOS/watchOS/tvOS/visionOS 버전의 시뮬레이터 런타임 다운로드/설치 (대소문자 구분하여 작성해야 함):

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{런타임_버전}}"`

- 런타임 아카이브를 처음 다운로드할 위치 설정 (기본값은 `~/Downloads`):

`xcodes runtimes {{download|install}} {{런타임_이름}} --directory {{경로/대상/폴더}}`

- 시뮬레이터가 성공적으로 설치된 후에도 다운로드한 아카이브 삭제하지 않기:

`xcodes runtimes install {{런타임_이름}} --keep-archive`

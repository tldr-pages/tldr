# xcodes

> 여러 Xcode 버전을 다운로드, 설치 및 관리.
> 같이 보기: `xcodes runtimes`.
> 더 많은 정보: <https://github.com/xcodesorg/xcodes>.

- 설치된 모든 Xcode 버전 나열:

`xcodes installed`

- 사용 가능한 모든 Xcode 버전 나열:

`xcodes list`

- 버전 번호 또는 경로를 지정하여 Xcode 버전 선택:

`xcodes select {{xcode_버전|경로/대상/Xcode.app}}`

- 특정 Xcode 버전 다운로드 및 설치:

`xcodes install {{xcode_버전}}`

- 최신 Xcode 릴리스를 설치하고 선택:

`xcodes install --latest --select`

- 특정 Xcode 버전 아카이브를 주어진 디렉토리에 다운로드(설치하지 않음):

`xcodes download {{xcode_버전}} --directory {{경로/대상/폴더}}`

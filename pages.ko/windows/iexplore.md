# iexplore

> Microsoft Internet Explorer.
> 참고: 이 프로그램은 최신 브라우저(예: `msedge`)로 대체되어 더 이상 유지 관리되지 않음.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/general-info/hh826025(v=vs.85)>.

- 지정한 URL 또는 파일 열기:

`iexplore {{https://example.com|경로\대상\파일.html}}`

- InPrivate 모드로 열기:

`iexplore -private {{example.com}}`

- 키오스크([k]iosk) 또는 애플리케이션 모드(도구 모음, 주소 표시줄, 버튼 등을 숨김)로 열기:

`iexplore -k {{example.com}}`

- 확장([ext]ensions/add-ons) 기능을 비활성화한 상태로 열기:

`iexplore -extoff {{example.com}}`

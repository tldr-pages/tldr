# microsoft-edge

> Google에서 개발한 Chromium 웹 브라우저를 기반으로 Microsoft가 개발한 현대적인 웹 브라우저.
> 이 명령은 Windows에서는 `msedge`로 사용 가능합니다.
> 참고: `chromium`의 추가 명령 인수도 Microsoft Edge 제어에 사용할 수 있습니다.
> 더 많은 정보: <https://microsoft.com/edge>.

- 특정 URL 또는 파일 열기:

`microsoft-edge {{https://example.com|경로/대상/파일.html}}`

- InPrivate 모드로 열기:

`microsoft-edge --inprivate {{example.com}}`

- 새 창에서 열기:

`microsoft-edge --new-window {{example.com}}`

- 애플리케이션 모드로 열기 (툴바, URL 바, 버튼 등 없이):

`microsoft-edge --app={{https://example.com}}`

- 프록시 서버 사용:

`microsoft-edge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 사용자 지정 프로필 디렉토리로 열기:

`microsoft-edge --user-data-dir={{경로/대상/폴더}}`

- CORS 검증 없이 열기 (API 테스트에 유용):

`microsoft-edge --user-data-dir={{경로/대상/폴더}} --disable-web-security`

- 각 탭이 열릴 때마다 DevTools 창 열기:

`microsoft-edge --auto-open-devtools-for-tabs`

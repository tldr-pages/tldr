# msedge

> 마이크로소프트에서 개발한 최신 웹 브라우저로, 구글에서 개발한 크로미움 웹 브라우저를 기반으로 합니다.
> 이 명령어는 다른 플랫폼에서는 `microsoft-edge`로 사용할 수 있습니다.
> 참고: `chromium`에서 추가 명령어 인수로 Microsoft Edge를 제어할 수 있습니다.
> 더 많은 정보: <https://microsoft.com/edge>.

- 특정 URL 또는 파일 열기:

`msedge {{https://example.com|경로\대상\파일.html}}`

- InPrivate 모드로 열기:

`msedge --inprivate {{example.com}}`

- 새 창으로 열기:

`msedge --new-window {{example.com}}`

- 애플리케이션 모드로 열기 (도구 모음, URL 표시줄, 버튼 등 없음):

`msedge --app={{https://example.com}}`

- 프록시 서버 사용:

`msedge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 사용자 데이터 디렉토리 사용:

`msedge --user-data-dir={{경로\대상\디렉토리}}`

- CORS 유효성 검사 없이 열기 (API 테스트에 유용):

`msedge --user-data-dir={{경로\대상\디렉토리}} --disable-web-security`

- 각 탭 열릴 때마다 DevTools 창 열기:

`msedge --auto-open-devtools-for-tabs`

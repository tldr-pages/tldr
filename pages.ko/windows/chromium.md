# chromium

> 주로 Google에서 개발 및 유지 관리하는 오픈 소스 웹 브라우저.
> 참고: 원하는 웹 브라우저에 따라 `chromium` 명령을 `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera`, 또는 `vivaldi`로 대체해야 할 수 있습니다.
> 더 많은 정보: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 특정 URL 또는 파일 열기:

`chromium {{https://example.com|경로/대상/파일.html}}`

- 시크릿 모드로 열기 (Microsoft Edge의 경우 `--inprivate` 사용):

`{{chromium --incognito|msedge --inprivate}} {{example.com}}`

- 새 창으로 열기:

`chromium --new-window {{example.com}}`

- 애플리케이션 모드로 열기 (툴바, URL 바, 버튼 등 없이):

`chromium --app={{https://example.com}}`

- 프록시 서버 사용:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 사용자 정의 프로필 디렉토리로 열기:

`chromium --user-data-dir={{경로/대상/폴더}}`

- CORS 검증 없이 열기 (API 테스트에 유용):

`chromium --user-data-dir={{경로/대상/폴더}} --disable-web-security`

- 열리는 각 탭에 대해 개발자 도구 창과 함께 열기:

`chromium --auto-open-devtools-for-tabs`

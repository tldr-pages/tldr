# chromium

> 구글에서 제공하는 오픈소스 웹 브라우저.
> 더 많은 정보: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 파일 열기:

`chromium {{경로/파일명.html}}`

- URL 열기:

`chromium {{example.com}}`

- 익명으로 열기:

`chromium --incognito {{example.com}}`

- 새 창에서 열기:

`chromium --new-window {{example.com}}`

- 앱 모드로 열기 (툴바, URL 바, 버튼 등 제외):

`chromium --app='{{https://example.com}}'`

- 프록시 서버 사용:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

# qutebrowser

> PyQt5 기반의 키보드 구동, vim 스타일 웹 브라우저.
> 더 많은 정보: <https://qutebrowser.org/doc/qutebrowser.1.html>.

- 지정된 저장소 디렉터리로 qutebrowser 열기:

`qutebrowser --basedir {{경로/대상/폴더}}`

- 임시 설정으로 qutebrowser 인스턴스 열기:

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- 지정된 이름의 세션을 복원하여 qutebrowser 인스턴스 열기:

`qutebrowser --restore {{세션_이름}}`

- 지정된 방법으로 모든 URL을 열며 qutebrowser 실행:

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- 임시 기본 디렉터리로 qutebrowser 열고 로그를 `stdout`에 JSON 형식으로 출력:

`qutebrowser --temp-basedir --json-logging`

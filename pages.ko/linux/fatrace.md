# fatrace

> 파일 접근 이벤트 보고.
> 더 많은 정보: <https://manned.org/fatrace>.

- 모든 마운트된 파일시스템의 파일 접근 이벤트를 `stdout`에 출력:

`sudo fatrace`

- 현재 디렉토리의 마운트에서 파일 접근 이벤트를 타임스탬프와 함께 `stdout`에 출력:

`sudo fatrace {{[-c|--current-mount]}} {{[-t|--timestamp]}}`

# inotifywait

> 파일 변경을 대기합니다.
> 더 많은 정보: <https://manned.org/inotifywait>.

- 특정 파일의 이벤트를 감시하고 첫 번째 이벤트 이후 종료:

`inotifywait {{경로/대상/파일}}`

- 특정 파일의 이벤트를 종료하지 않고 지속적으로 감시:

`inotifywait --monitor {{경로/대상/파일}}`

- 폴더의 이벤트를 재귀적으로 감시:

`inotifywait --monitor --recursive {{경로/대상/폴더}}`

- 정규 표현식과 일치하는 파일을 제외하고 폴더의 변경 사항 감시:

`inotifywait --monitor --recursive --exclude "{{정규_표현식}}" {{경로/대상/폴더}}`

- 30초 동안 이벤트가 발생하지 않으면 종료하며 파일의 변경 사항 감시:

`inotifywait --monitor --timeout {{30}} {{경로/대상/파일}}`

- 파일 수정 이벤트만 감시:

`inotifywait --event {{modify}} {{경로/대상/파일}}`

- 이벤트만 출력하고 상태 메시지는 출력하지 않고 파일 감시:

`inotifywait --quiet {{경로/대상/파일}}`

- 파일에 접근할 때 명령 실행:

`inotifywait --event {{access}} {{경로/대상/파일}} && {{명령}}`

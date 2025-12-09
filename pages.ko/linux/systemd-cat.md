# systemd-cat

> 파이프라인 또는 프로그램의 출력 스트림을 systemd 저널과 연결.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cat.html>.

- 지정한 명령의 출력을 저널에 기록 (모든 출력 스트림이 캡처됨):

`systemd-cat {{명령}}`

- 파이프라인의 출력을 저널에 기록 (`stderr`는 터미널에 연결된 상태 유지):

`{{명령}} | systemd-cat`

# pueue add

> 실행할 작업을 대기열에 추가.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 대기열에 임의의 명령 추가:

`pueue add {{명령어}}`

- 플래그 또는 인수를 명령에 전달하여 대기열에 추가:

`pueue add -- {{명령어 --인수 -f}}`

- 대기열에서 첫 번째인 경우 시작하지 않도록 명령 추가:

`pueue add --stashed -- {{rsync --archive --compress /local/directory /remote/directory}}`

- 그룹에 명령 추가 및 즉시 시작, 그룹 관리에 대해서는 `pueue group` 참고:

`pueue add --immediate --group "{{CPU_집중}}" -- {{ffmpeg -i input.mp4 frame_%d.png}}`

- 명령 추가 및 9번과 12번 명령이 성공적으로 완료된 후 시작:

`pueue add --after {{9}} {{12}} --group "{{토렌트}}" -- {{transmission-cli torrent_file.torrent}}`

- 일정 시간 후 레이블을 붙여 명령 추가, 유효한 날짜 형식에 대해서는 `pueue enqueue` 참고:

`pueue add --label "{{큰 파일 압축}}" --delay "{{수요일 10:30pm}}" -- "{{7z a compressed_file.7z large_file.xml}}"`

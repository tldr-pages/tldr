# cancel

> 프린트 작업 취소.
> 참고: `lp`, `lpmove`, `lpstat`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- 기본 프린터의 현재 작업을 취소 (`lpoptions -d {{printer}}`로 설정):

`cancel`

- 특정 사용자([u]ser)가 소유한 기본 프린터의 작업을 취소:

`cancel -u {{사용자명}}`

- 특정 프린터의 현재 작업을 취소:

`cancel {{프린터}}`

- 특정 프린터에서 특정 작업을 취소:

`cancel {{프린터}}-{{작업_아이디}}`

- 모든 프린터의 모든([a]ll) 작업을 취소:

`cancel -a`

- 특정 프린터의 모든([a]ll) 작업을 취소:

`cancel -a {{프린터}}`

- 특정 서버의 현재 작업을 취소한 다음 작업 데이터 파일을 삭제([x]):

`cancel -h {{서버}} -x`

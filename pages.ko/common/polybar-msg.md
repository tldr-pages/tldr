# polybar-msg

> `polybar`를 프로세스 간 메시징(IPC)을 사용하여 제어.
> 참고: IPC는 기본적으로 비활성화되어 있으며, Polybar 설정에서 `enable-ipc = true`로 설정하여 활성화할 수 있습니다.
> 더 많은 정보: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

- 바 종료:

`polybar-msg cmd quit`

- 바를 제자리에서 재시작:

`polybar-msg cmd restart`

- 바 숨기기 (이미 바가 숨겨져 있으면 아무 작업도 하지 않음):

`polybar-msg cmd hide`

- 바 다시 표시 (바가 숨겨져 있지 않으면 아무 작업도 하지 않음):

`polybar-msg cmd show`

- 숨김/표시 전환:

`polybar-msg cmd toggle`

- 모듈 작업 실행 (데이터 문자열은 선택 사항):

`polybar-msg action "#{{모듈_이름}}.{{작업_이름}}.{{데이터_문자열}}"`

- 특정 Polybar 인스턴스에만 메시지 전송 (기본적으로 모든 인스턴스):

`polybar-msg -p {{pid}} {{cmd|action}} {{페이로드}}`

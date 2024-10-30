# systemd-notify

> 시작 완료 및 기타 데몬 상태 변경 사항을 서비스 관리자에게 알림.
> 이 명령은 systemd 서비스 스크립트 외부에서는 쓸모가 없습니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-notify.html>.

- 서비스가 초기화를 완료하고 완전히 시작되었음을 systemd에 알림. 서비스가 들어오는 요청을 처리할 준비가 되었을 때 호출해야 함:

`systemd-notify --booted`

- 서비스가 들어오는 연결을 처리하거나 작업을 수행할 준비가 되었음을 systemd에 신호:

`systemd-notify --ready`

- systemd에 사용자 정의 상태 메시지 제공 (`systemctl status`에 의해 표시됨):

`systemd-notify --status="{{여기에 사용자 정의 상태 메시지를 추가하세요...}}"`

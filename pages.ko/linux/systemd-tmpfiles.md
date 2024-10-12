# systemd-tmpfiles

> 휘발성 및 임시 파일과 디렉토리를 생성, 삭제 및 정리합니다.
> 이 명령어는 시스템 부팅 시 systemd 서비스에 의해 자동으로 호출되며, 수동으로 실행할 필요는 거의 없습니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>.

- 설정에 따라 파일과 디렉토리 생성:

`systemd-tmpfiles --create`

- 나이 매개변수가 설정된 파일과 디렉토리 정리:

`systemd-tmpfiles --clean`

- 설정에 따라 파일과 디렉토리 제거:

`systemd-tmpfiles --remove`

- 사용자별 설정 적용:

`systemd-tmpfiles --create --user`

- 초기 부팅 시 실행할 라인 실행:

`systemd-tmpfiles --create --boot`

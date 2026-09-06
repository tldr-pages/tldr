# akmods

> Fedora/RHEL-based 기반 배포판을 위한 자동 커널 모듈 관리 시스템.
> 커널이 업데이트되면 외부 kernel 모듈을 동적으로 다시 빌드 (예: NVIDIA 드라이버).
> 더 많은 정보: <https://manned.org/akmods>.

- 현재 실행중인 커널에서 누락 또는 오래된 모든 커널 모듈 다시 빌드:

`sudo akmods`

- 현재 상태와 관계없이 모든 커널 모듈을 강제로 다시 빌드:

`sudo akmods --rebuild --force`

- 지정한 kernel 버전용 모듈 다시 빌드:

`sudo akmods --kernel {{커널_버전}}`

- 백그라운드 akmods 서비스의 현재 상태 및 로그 세부 정보 표시:

`systemctl status akmods`

# systemd-machine-id-setup

> 설치 시 `/etc/machine-id`에 저장된 머신 ID를 프로비저닝된 ID 또는 무작위로 생성된 ID로 초기화.
> 참고: 이러한 명령은 높은 권한이 필요하므로 항상 `sudo`를 사용하여 실행해야 합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>.

- 생성되거나 커밋된 머신 ID 출력:

`systemd-machine-id-setup --print`

- 이미지 정책 지정:

`systemd-machine-id-setup --image-policy={{your_policy}}`

- 출력을 JSON 형식으로 표시:

`sudo systemd-machine-id-setup --json=pretty`

- 디렉터리 트리 대신 디스크 이미지에서 작업 수행:

`systemd-machine-id-setup --image={{/경로/대상/이미지}}`

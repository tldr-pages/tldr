# atomupd-manager

> SteamOS 업데이트 관리.
> 더 많은 정보: <https://github.com/evlaV/atomupd-daemon>.

- 사용 가능한 업데이트 확인:

`sudo atomupd-manager check`

- 특정 이미지 버전으로 업데이트:

`sudo atomupd-manager update {{버전_아이디}}`

- 현재 추적 중인 업데이트 채널 출력:

`atomupd-manager tracked-branch`

- 사용 가능한 업데이트 채널 목록 출력:

`atomupd-manager list-branches`

- 특정 업데이트 채널로 전환:

`sudo atomupd-manager switch-branch {{stable|beta|preview|rc|bc|pc|main}}`

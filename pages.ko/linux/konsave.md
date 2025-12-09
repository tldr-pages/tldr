# konsave

> 한 번의 명령으로 Linux 사용자 설정을 저장하고 적용.
> 더 많은 정보: <https://github.com/Prayag2/konsave>.

- 현재 설정을 프로필로 저장:

`konsave --save {{프로필_이름}}`

- 프로필 적용:

`konsave --apply {{프로필_이름}}`

- 현재 설정을 프로필로 저장하며, 동일한 이름의 기존 프로필이 있을 경우 덮어쓰기:

`konsave -s {{프로필_이름}} --force`

- 모든 프로필 나열:

`konsave --list`

- 프로필 제거:

`konsave --remove {{프로필_이름}}`

- 프로필을 `.knsv`로 내보내기하여 홈 디렉토리에 저장:

`konsave --export-profile {{프로필_이름}}`

- `.knsv` 프로필 가져오기:

`konsave --import-profile {{경로/대상/프로필_이름.knsv}}`

# settings

> Android OS에 대한 정보 얻기.
> 더 많은 정보: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- `global` 네임스페이스의 설정 목록을 표시:

`settings list {{global}}`

- 특정 설정의 값 가져오기:

`settings get {{global}} {{airplane_mode_on}}`

- 특정 설정 값 설정:

`settings put {{system}} {{screen_brightness}} {{42}}`

- 특정 설정 삭제:

`settings delete {{secure}} {{screensaver_enabled}}`

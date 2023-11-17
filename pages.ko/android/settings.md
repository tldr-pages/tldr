# settings

> Android OS에 대한 정보 얻기.
> 더 많은 정보: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- `global` 네임스페이스의 설정 목록을 표시:

`settings list {{글로벌}}`

- 특정 설정의 값 가져오기:

`settings get {{글로벌}} {{비행기_모드_온}}`

- 특정 설정 값 설정:

`settings put {{시스템}} {{스크린_밝기}} {{42}}`

- 특정 설정 삭제:

`settings delete {{보안}} {{화면_보호기_활성화}}`

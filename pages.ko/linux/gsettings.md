# gsettings

> 스키마 검증을 통해 dconf 설정을 조회하고 수정.
> 더 많은 정보: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- 키의 값을 설정 (키가 존재하지 않거나 값이 범위를 벗어난 경우 실패):

`gsettings set {{org.example.schema}} {{예제-키}} {{값}}`

- 키의 값 또는 `dconf`에 설정되지 않은 경우 스키마에 제공된 기본값 출력:

`gsettings get {{org.example.schema}} {{예제-키}}`

- 키를 해제하여 스키마 기본값 사용:

`gsettings reset {{org.example.schema}} {{예제-키}}`

- 모든 (이동 불가능한) 스키마, 키 및 값 표시:

`gsettings list-recursively`

- 하나의 스키마에서 모든 키 및 값 (설정되지 않은 경우 기본값) 표시:

`gsettings list-recursively {{org.example.schema}}`

- 키에 대해 스키마가 허용하는 값 표시 (enum 키에 유용):

`gsettings range {{org.example.schema}} {{예제-키}}`

- 키의 사람이 읽을 수 있는 설명 표시:

`gsettings describe {{org.example.schema}} {{예제-키}}`

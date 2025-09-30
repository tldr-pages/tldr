# ykman openpgp

> OpenPGP YubiKey 애플리케이션 관리.
> 참고: 일부 설정을 위해 `gpg --card-edit`를 사용해야 합니다.
> 더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>.

- OpenPGP 애플리케이션에 대한 일반 정보 표시:

`ykman openpgp info`

- 사용자 PIN, 재설정 코드 및 관리자 PIN의 재시도 횟수 설정:

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- 사용자 PIN, 재설정 코드 또는 관리자 PIN 변경:

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- OpenPGP 애플리케이션 초기화 (관리자 PIN 재시도 횟수를 초과한 후 수행해야 합니다):

`ykman openpgp reset`

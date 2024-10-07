# systemd-cryptenroll

> LUKS2로 암호화된 장치를 잠금 해제하는 데 사용되는 방법을 대화식으로 등록하거나 제거합니다. 별도로 지정하지 않으면 암호를 사용하여 장치를 잠금 해제합니다.
> 시스템 부팅 시 파티션을 잠금 해제하려면 `/etc/crypttab` 파일이나 initramfs를 업데이트해야 합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- 새 비밀번호 등록 (`cryptsetup luksAddKey`와 유사):

`systemd-cryptenroll --password {{경로/대상/luks2_블록_장치}}`

- 새 복구 키 등록 (즉, 대체로 사용할 수 있는 무작위 생성 암호):

`systemd-cryptenroll --recovery-key {{경로/대상/luks2_블록_장치}}`

- 사용 가능한 토큰 목록 나열 또는 새 PKCS#11 토큰 등록:

`systemd-cryptenroll --pkcs11-token-uri {{list|auto|pkcs11_토큰_uri}} {{경로/대상/luks2_블록_장치}}`

- 사용 가능한 FIDO2 장치 목록 나열 또는 새 FIDO2 장치 등록 (`auto`는 토큰이 하나만 연결되어 있을 때 장치 이름으로 사용 가능):

`systemd-cryptenroll --fido2-device {{list|auto|경로/대상/fido2_hidraw_장치}} {{경로/대상/luks2_블록_장치}}`

- 사용자 인증(생체 인식)과 함께 새 FIDO2 장치 등록:

`systemd-cryptenroll --fido2-device {{auto|경로/대상/fido2_hidraw_장치}} --fido2-with-user-verification yes {{경로/대상/luks2_블록_장치}}`

- FIDO2 장치를 사용하여 잠금 해제하고 새 FIDO2 장치 등록:

`systemd-cryptenroll --unlock-fido2-device {{경로/대상/fido2_hidraw_잠금_해제_장치}} --fido2-device {{경로/대상/fido2_hidraw_등록_장치}} {{경로/대상/luks2_블록_장치}}`

- TPM2 보안 칩 등록 (보안 부팅 정책 PCR만) 및 추가적인 영문자 PIN 필요:

`systemd-cryptenroll --tpm2-device {{auto|경로/대상/tpm2_블록_장치}} --tpm2-with-pin yes {{경로/대상/luks2_블록_장치}}`

- 모든 빈 비밀번호/모든 비밀번호/모든 FIDO2 장치/모든 PKCS#11 토큰/모든 TPM2 보안 칩/모든 복구 키/모든 방법 제거:

`systemd-cryptenroll --wipe-slot {{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{경로/대상/luks2_블록_장치}}`

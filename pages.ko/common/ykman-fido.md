# ykman fido

> YubiKey FIDO 애플리케이션 관리.
> 더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/FIDO_Commands.html>.

- FIDO2 애플리케이션에 대한 일반 정보 표시:

`ykman fido info`

- FIDO PIN 변경:

`ykman fido access change-pin`

- YubiKey에 저장된 거주 인증서 나열:

`ykman fido credentials list`

- YubiKey에서 거주 인증서 삭제:

`ykman fido credentials delete {{id}}`

- YubiKey에 저장된 지문 나열 (지문 센서가 있는 키 필요):

`ykman fido fingerprints list`

- YubiKey에 새 지문 추가:

`ykman fido fingerprints add {{이름}}`

- YubiKey에서 지문 삭제:

`ykman fido fingerprints delete {{이름}}`

- 모든 FIDO 자격 증명 삭제 (PIN 재시도 횟수를 초과한 후 수행해야 함):

`ykman fido reset`

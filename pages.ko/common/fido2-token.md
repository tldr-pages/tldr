# fido2-token

> FIDO2 인증 장치를 검색하고 관리.
> 더 많은 정보: <https://developers.yubico.com/libfido2/Manuals/fido2-token.html>.

- 모든 FIDO2 인증 장치 나열:

`fido2-token -L`

- 특정 인증 장치에 대한 정보 표시:

`fido2-token -I {{장치}}`

- 인증 장치에 저장된 탐색 가능 자격 증명(discoverable credentials)이 있는 신뢰 당사자(RP) 나열:

`fido2-token -L -r {{장치}}`

- 특정 신뢰 당사자(일반적으로 도메인 이름)에 대한 탐색 가능 자격 증명 나열:

`fido2-token -L -k {{신뢰_당사자_id}} {{장치}}`

- base64로 인코딩된 ID로 탐색 가능 자격 증명 삭제:

`fido2-token -D -i {{자격_증명_id}} {{장치}}`

- 인증 장치의 PIN 설정 또는 변경:

`fido2-token {{-S|-C}} {{장치}}`

- 인증 장치를 공장 기본값으로 재설정:

`fido2-token -R {{장치}}`

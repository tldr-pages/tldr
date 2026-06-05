# pkcs11-tool

> PKCS #11 보안 토큰 관리 및 사용 유틸리티.
> 더 많은 정보: <https://github.com/OpenSC/OpenSC/wiki/Using-pkcs11-tool-and-OpenSSL>.

- 특정 모듈을 사용하여 슬롯과 해당 토큰 목록 표시 (예: `/usr/lib/softhsm/libsofthsm2.so`):

`pkcs11-tool --module {{경로/대상/모듈.so}} {{[-L|--list-slots]}} {{[-T|--list-token-slots]}}`

- 특정 슬롯의 객체 목록 표시 (참고: `slot_id`는 "Slot X" 형태의 인덱스와 다름):

`pkcs11-tool {{[-O|--list-objects]}} {{[-p|--pin]}} {{auth_pin}} --slot {{슬롯_아이디}}`

- 특정 라벨과 타입을 가진 새로운 객체 생성:

`pkcs11-tool --slot {{슬롯_아이디}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{라벨}}" {{[-d|--id]}} {{01}} {{[-w|--write-object]}} {{경로/대상/cert.crt}}`

- 라벨과 타입으로 특정 객체 삭제:

`pkcs11-tool --slot {{슬롯_아이디}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{라벨}}" {{[-b|--delete-object]}}`

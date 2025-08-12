# sbctl

> 사용자 친화적인 보안 부트 키 관리자.
> 참고: Microsoft의 인증서를 등록하지 않으면 시스템이 손상될 수 있습니다. <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>을 참조하세요.
> 더 많은 정보: <https://github.com/Foxboron/sbctl#usage>.

- 현재 보안 부트 상태 표시:

`sbctl status`

- 사용자 정의 보안 부트 키 생성 (기본적으로 모든 것은 `/var/lib/sbctl`에 저장):

`sbctl create-keys`

- 사용자 정의 보안 부트 키 및 Microsoft의 UEFI 공급업체 인증서 등록:

`sbctl enroll-keys {{[-m|--microsoft]}}`

- `/etc/sbctl/sbctl.conf`의 설정에 따라 `create-keys`와 `enroll-keys` 자동 실행:

`sbctl setup --setup`

- 생성된 키로 EFI 바이너리에 서명하고 파일을 데이터베이스에 저장:

`sbctl sign {{[-s|--save]}} {{경로/대상/efi_바이너리}}`

- 저장된 모든 파일 다시 서명:

`sbctl sign-all`

- EFI 시스템 파티션의 모든 EFI 실행 파일이 서명되었는지 확인:

`sbctl verify`

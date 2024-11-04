# ykman

> YubiKey Manager - YubiKey 구성 도구.
> 여러 개의 YubiKey가 연결된 경우, 하위 명령어 앞에 `--device {{serial_number}}`를 추가해야 합니다.
> 더 많은 정보: <https://docs.yubico.com/software/yubikey/tools/ykman/index.html>.

- YubiKey에 대한 일반 정보 표시 (일련번호, 펌웨어 버전, 기능 등):

`ykman info`

- 연결된 YubiKey를 짧고 한 줄로 설명 (일련번호 포함):

`ykman list`

- 애플리케이션 활성화 및 비활성화에 대한 문서 보기:

`tldr ykman config`

- FIDO 애플리케이션 관리에 대한 문서 보기:

`tldr ykman fido`

- OATH 애플리케이션 관리에 대한 문서 보기:

`tldr ykman oath`

- OpenPGP 애플리케이션 관리에 대한 문서 보기:

`tldr ykman openpgp`

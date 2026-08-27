# sq

> 최신 OpenPGP 명령줄 도구.
> 관련 항목: `gpg`.
> 더 많은 정보: <https://sequoia-pgp.gitlab.io/sequoia-sq/man/sq.1.html>.

- 비밀번호를 사용하여 파일 암호화 (대칭 암호화):

`sq encrypt --with-password --without-signature {{경로/대상/파일}} --output {{경로/대상/파일.pgp}}`

- 비밀번호로 보호된 파일 복호화:

`sq decrypt {{경로/대상/파일.pgp}} --output {{경로/대상/파일}}`

- OpenPGP 파일의 메타데이터와 구조 확인:

`sq inspect {{경로/대상/파일.pgp}}`

- 인증서 파일을 사용하여 분리된 서명 검증:

`sq verify --signer-file {{path/to/signer.asc}} --signature-file {{경로/대상/파일.sig}} {{경로/대상/파일}}`

- 인증서 파일을 사용하여 포함된 평문(cleartext)  서명 검증:

`sq verify --signer-file {{path/to/signer.asc}} --cleartext {{경로/대상/파일}}`

- 자신의 키를 생성하여, 로컬 키 저장소에 저장:

`sq key generate --own-key --name {{이름}} --email {{이름@이메일}}`

- 로컬 키 저장소에서 관리하는 모든 비밀 키 또는 인증서 목록 표시:

`sq {{key|cert}} list`

- 현재 설정 및 저장소 경로 목록 표시:

`sq config inspect paths`

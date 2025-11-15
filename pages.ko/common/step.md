# step

> 사용하기 쉬운 CLI 도구로, 공개 키 기반 구조(PKI) 시스템 및 워크플로를 구축, 운영 및 자동화하는 데 도움을 줍니다.
> 같이 보기: `openssl`.
> 더 많은 정보: <https://smallstep.com/docs/step-cli/>.

- 인증서의 내용을 검사:

`step certificate inspect {{경로/대상/인증서.crt}}`

- 루트 CA 인증서 및 키 생성 (개인 키 비밀번호 보호를 건너뛰려면 `--no-password --insecure` 추가):

`step certificate create "{{예시 루트 CA}}" {{경로/대상/root-ca.crt}} {{경로/대상/root-ca.key}} --profile root-ca`

- 특정 호스트명을 위한 인증서를 생성하고 루트 CA로 서명 (CSR 생성을 생략하여 간소화 가능):

`step certificate create {{hostname.example.com}} {{경로/대상/hostname.crt}} {{경로/대상/hostname.key}} --profile leaf --ca {{경로/대상/root-ca.crt}} --ca-key {{경로/대상/root-ca.key}}`

- 인증서 체인 검증:

`step certificate verify {{경로/대상/호스트명.crt}} --roots {{경로/대상/root-ca.crt}} --verbose`

- PEM 형식 인증서를 DER로 변환하여 디스크에 저장:

`step certificate format {{경로/대상/인증서.pem}} --out {{경로/대상/인증서.der}}`

- 시스템 기본 신뢰 저장소에 루트 인증서를 설치하거나 제거:

`step certificate {{install|uninstall}} {{경로/대상/root-ca.crt}}`

- RSA/EC 개인 및 공개 키 쌍 생성 (개인 키 비밀번호 보호를 건너뛰려면 `--no-password --insecure` 추가):

`step crypto keypair {{경로/대상/공개_키}} {{경로/대상/비밀_키}} --kty {{RSA|EC}}`

- 하위 명령에 대한 도움말 표시:

`step {{path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh}} --help`

# vt

> VirusTotal의 명령줄 인터페이스.
> 이 명령을 사용하려면 VirusTotal 계정의 API 키가 필요합니다.
> 더 많은 정보: <https://github.com/VirusTotal/vt-cli>.

- 특정 파일을 바이러스 검사:

`vt scan file {{경로/대상/파일}}`

- URL을 바이러스 검사:

`vt scan url {{url}}`

- 특정 분석에 대한 정보 표시:

`vt analysis {{파일_ID|분석_ID}}`

- 암호화된 Zip 형식으로 파일 다운로드 (프리미엄 계정 필요):

`vt download {{파일_ID}} --output {{경로/대상/폴더}} --zip --zip-password {{비밀번호}}`

- `vt`를 초기화하거나 재초기화하여 API 키를 대화식으로 입력:

`vt init`

- 도메인에 대한 정보 표시:

`vt domain {{url}}`

- 특정 URL에 대한 정보 표시:

`vt url {{url}}`

- 특정 IP 주소에 대한 정보 표시:

`vt domain {{IP_주소}}`

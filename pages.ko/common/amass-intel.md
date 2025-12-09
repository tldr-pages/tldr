# amass intel

> 루트 도메인 및 ASN과 같은 조직에 대한 오픈 소스 정보 수집.
> 더 많은 정보: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- IP 주소([addr]ess) 범위에서 루트 도메인 찾기:

`amass intel -addr {{192.168.0.1-254}}`

- 활성 정찰 방법을 사용:

`amass intel -active -addr {{192.168.0.1-254}}`

- 도메인([d]omain)과 관련된 루트 도메인 찾기:

`amass intel -whois -d {{도메인_이름}}`

- 조직([org]anisation)에 속하는 ASN 찾기:

`amass intel -org {{조직_이름}}`

- 주어진 자율 시스템 번호에 속하는 루트 도메인 찾기:

`amass intel -asn {{asn}}`

- 결과를 텍스트 파일에 저장:

`amass intel -o {{출력_파일}} -whois -d {{도메인_이름}}`

- 사용 가능한 모든 데이터 소스 나열:

`amass intel -list`

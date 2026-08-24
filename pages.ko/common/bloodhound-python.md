# bloodhound-python

> Active Directory 관계를 열거하기 위해 사용하는 BloodHound용 Python 수집 도구.
> 더 많은 정보: <https://github.com/dirkjanm/BloodHound.py#usage>.

- 기본 수집 방법을 사용하여 모든 데이터를 수집 (그룹, 세션, 트러스트 포함):

`bloodhound-python --username {{사용자명}} --password {{비밀번호}} --domain {{도메인}}`

- 평문 비밀번호 없이 Kerberos 인증을 사용하여 데이터를 수집:

`bloodhound-python --collectionmethod {{All}} --kerberos --domain {{도메인}}`

- 비밀번호 대신 NTLM 해시를 사용하여 인증:

`bloodhound-python --collectionmethod {{All}} --username {{사용자명}} --hashes {{LM:NTLM}} --domain {{도메인}}`

- DNS 조회에 사용할 사용자 지정 네임서버를 선택:

`bloodhound-python --collectionmethod {{All}} --username {{사용자명}} --password {{비밀번호}} --domain {{도메인}} --nameserver {{네임서버}}`

- 출력 파일을 압축된 ZIP 아카이브로 저장:

`bloodhound-python --collectionmethod {{All}} --username {{사용자명}} --password {{비밀번호}} --domain {{도메인}} --zip`

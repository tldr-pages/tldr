# getTGT.py

> Ticket Granting Ticket (TGT) 요청.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 비밀번호를 사용하여 TGT 요청:

`getTGT.py {{도메인}}/{{사용자명}}:{{비밀번호}}`

- NTLM 해시를 사용하여 TGT 요청:

`getTGT.py -hashes {{LM_Hash}}:{{NT_Hash}} {{도메인}}/{{사용자명}}`

- Kerberos 인증 사용 (기존 ccache, 비밀번호 불필요):

`getTGT.py -k -no-pass {{도메인}}/{{사용자명}}`

- AES키를 사용하여 TGT 요청 (128 또는 256비트):

`getTGT.py -aesKey {{aes_key}} {{도메인}}/{{사용자명}}`

- 도메인 컨트롤러 IP 지정:

`getTGT.py -dc-ip {{도메인_controller_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- 특정 SPN에 대해 직접 서비스 티켓 요청 (AS-REQ):

`getTGT.py -service {{SPN}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

# getST.py

> Kerberos Service Ticket (TGS) 요청.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 특정 SPN에 대한 서비스 티켓 요청:

`getST.py {{도메인}}/{{사용자명}}:{{비밀번호}} -spn {{서비스}}/{{대상}}`

- NTLM 해시 (pass-the-hash)를 사용하여 티켓 요청:

`getST.py -hashes {{LM_Hash}}:{{NT_Hash}} {{도메인}}/{{사용자명}} -spn {{서비스}}/{{대상}}`

- 기존 Kerberos ccache 파일을 사용해 티켓 요청:

`getST.py -no-pass -k {{도메인}}/{{사용자명}} -spn {{서비스}}/{{대상}}`

- S4U2Self를 통해 다른 사용자로 가장 (위임 권한 필요) 수행:

`getST.py -k -impersonate {{타겟_사용자}} {{도메인}}/{{사용자명}} -spn {{서비스}}/{{대상}}`

- Force the ticket to be forwardable (Bronze Bit):

`getST.py -force-forwardable -k {{도메인}}/{{사용자명}} -spn {{서비스}}/{{대상}}`

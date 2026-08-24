# DumpNTLMInfo.py

> 인증정보 없이 원격 호스트에 대해 NTLM 인증을 수행하고, NTLMSSP 메시지에서 노출되는 정보를 추출.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 대상(SMB, 기본 포트 445)에서 NTLM 정보 추출:

`DumpNTLMInfo.py {{타겟}}`

- 특정 IP를 사용하여 NTLM 정보 추출:

`DumpNTLMInfo.py -target-ip {{타겟_주소}} {{타겟}}`

- 사용자 정의 포트 지정:

`DumpNTLMInfo.py -port {{포트}} {{타겟}}`

- RPC 프로토콜 (기본 포트 135) 사용하여 NTLM 정보 추출:

`DumpNTLMInfo.py -protocol RPC -port 135 {{타겟}}`

- 디버그 출력 활성화:

`DumpNTLMInfo.py -debug {{타겟}}`

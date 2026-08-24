# DumpNTLMInfo.py

> Perform NTLM authentication against a remote host without credentials and dump information leaked in the NTLMSSP message.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Dump NTLM info from target (SMB, default port 445):

`DumpNTLMInfo.py {{target}}`

- Dump NTLM info using a specific IP:

`DumpNTLMInfo.py -target-ip {{target_ip}} {{target}}`

- Specify a custom port:

`DumpNTLMInfo.py -port {{port}} {{target}}`

- Dump NTLM info using RPC protocol (default port 135):

`DumpNTLMInfo.py -protocol RPC -port 135 {{target}}`

- Turn on debug output:

`DumpNTLMInfo.py -debug {{target}}`

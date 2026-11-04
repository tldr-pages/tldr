# mimikatz kerberos

> Kerberos 티켓과 상호작용.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 현재 Kerberos 티켓 목록 표시:

`mimikatz "kerberos::list"`

- 모든 Kerberos 티켓 제거:

`mimikatz "kerberos::purge"`

- `.kirbi` 파일에서 Kerberos 티켓 주입:

`mimikatz "kerberos::ptt ticket.kirbi"`

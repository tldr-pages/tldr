# cmdkey

> 저장된 사용자 이름 및 비밀번호를 생성, 표시, 삭제.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- 모든 사용자 자격 증명 나열:

`cmdkey /list`

- 서버에 액세스하는 사용자의 자격 증명 저장:

`cmdkey /add:{{서버_이름}} /user:{{사용자_이름}}`

- 특정 대상의 자격 증명 삭제:

`cmdkey /delete {{대상_이름}}`

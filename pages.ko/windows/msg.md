# msg

> 사용자 또는 세션에 메시지 보내기.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- 특정 사용자 또는 세션에 메시지 보내기:

`msg {{사용자명|세션명|세션_아이디}} {{메시지}}`

- `stdin`에서 메시지 보내기:

`echo "{{메시지}}" | msg {{사용자명|세션명|세션_아이디}}`

- 특정 서버에 메시지 보내기:

`msg /server:{{서버명}} {{사용자명|세션명|세션_아이디}}`

- 현재 컴퓨터의 모든 사용자에게 메시지 보내기:

`msg *`

- 메시지 지연 설정 (초):

`msg /time:{{10}}`

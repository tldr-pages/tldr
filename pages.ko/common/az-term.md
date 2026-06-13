# az term

> 마켓플레이스주문을 통해 마켓플레이스 계약을 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/term>.

- 마켓플레이스 약관 인쇄:

`az term show --product "{{제품_식별자}}" --plan "{{플랜_식별자}}" --publisher "{{배포_식별자}}"`

- 마켓플레이스 약관에 동의:

`az term accept --product "{{제품_식별자}}" --plan "{{플랜_식별자}}" --publisher "{{배포_식별자}}"`

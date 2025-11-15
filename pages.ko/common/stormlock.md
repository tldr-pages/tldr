# stormlock

> 중앙 집중식 잠금 시스템.
> 더 많은 정보: <https://github.com/tmccombs/stormlock>.

- 리소스에 대한 임대 획득:

`stormlock acquire {{리소스}}`

- 주어진 리소스에 대한 주어진 임대 해제:

`stormlock release {{리소스}} {{임대_ID}}`

- 리소스에 대한 현재 임대 정보 표시 (있는 경우):

`stormlock current {{리소스}}`

- 주어진 리소스에 대한 임대가 현재 활성 상태인지 테스트:

`stormlock is-held {{리소스}} {{임대_ID}}`

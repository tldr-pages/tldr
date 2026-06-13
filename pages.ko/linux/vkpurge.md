# vkpurge

> `xbps`에 의해 남겨진 오래된 커널 버전을 나열하거나 제거합니다.
> `version` 인수는 셸 글롭을 지원합니다.
> 더 많은 정보: <https://man.voidlinux.org/vkpurge.8>.

- 제거 가능한 모든 커널 버전 나열 (또는 `version` 인수가 지정된 경우 해당 버전 나열):

`vkpurge list {{버전}}`

- 사용되지 않는 모든 커널 제거:

`vkpurge rm all`

- `version`과 일치하는 커널 버전 제거:

`vkpurge rm {{버전}}`

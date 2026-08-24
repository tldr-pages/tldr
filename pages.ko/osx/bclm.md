# bclm

> MacBook 배터리 충전 제한을 설정하는 도구.
> 더 많은 정보: <https://github.com/zackelia/bclm#usage>.

- 충전 제한을 약 80%로 설정 (Intel 모델에선, 실제 충전되는 양이 작을 수 있음):

`sudo bclm write {{77}}`

- 현재 충전 제한 값 확인:

`bclm read`

- 재부팅/smc 리셋 후에도 설정 유지:

`sudo bclm persist`

- 영구 설정 해제:

`sudo bclm unpersist`

# wacli sync

> WhatsApp 메시지를 로컬 저장소와 동기화.
> 관련 항목: `wacli auth`, `wacli messages list`.
> 더 많은 정보: <https://wacli.sh/sync.html>.

- 메시지 동기화:

`wacli sync`

- 메시지 한 번 동기화한 후에 종료:

`wacli sync --once`

- 사용자 지정 저장소를 사용해 메시지 동기화:

`wacli sync --store {{경로/대상/저장소}}`

- 사용자 지정 타임아웃을 설정하여 메시지 동기화:

`wacli sync --timeout {{10m}}`

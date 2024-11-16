# swapoff

> 스왑을 위한 장치 및 파일 비활성화.
> 참고: `경로/대상/파일`은 일반 파일이나 스왑 파티션을 가리킬 수 있습니다.
> 더 많은 정보: <https://manned.org/swapoff>.

- 지정된 스왑 영역 비활성화:

`swapoff {{경로/대상/파일}}`

- `/proc/swaps`의 모든 스왑 영역 비활성화:

`swapoff --all`

- 레이블로 스왑 파티션 비활성화:

`swapoff -L {{레이블}}`

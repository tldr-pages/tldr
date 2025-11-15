# ntpdate

> NTP를 통해 날짜 및 시간을 동기화하고 설정합니다.
> 더 많은 정보: <https://manned.org/ntpdate>.

- 날짜와 시간을 동기화하고 설정:

`sudo ntpdate {{호스트}}`

- 시간을 설정하지 않고 호스트에 질의:

`ntpdate -q {{호스트}}`

- 방화벽이 특권 포트를 차단하는 경우 비특권 포트를 사용:

`sudo ntpdate -u {{호스트}}`

- 시간을 `slewed` 대신 `settimeofday`를 사용하여 강제로 조정:

`sudo ntpdate -b {{호스트}}`

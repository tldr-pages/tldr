# getprop

> Android 시스템 속성에 대한 정보 보여주기.
> 더 많은 정보: <https://manned.org/getprop>.

- Android 시스템 속성에 대한 정보 표시:

`getprop`

- 특정 속성에 대한 정보 표시:

`getprop {{property}}`

- SDK API 수준 표시:

`getprop {{ro.build.version.sdk}}`

- Android 버전 표시:

`getprop {{ro.build.version.release}}`

- Android 기기 모델 표시:

`getprop {{ro.vendor.product.model}}`

- OEM 잠금 해제 상태 표시:

`getprop {{ro.oem_unlock_supported}}`

- Android's Wi-Fi 카드의 MAC 주소를 표시:

`getprop {{ro.boot.wifimacaddr}}`

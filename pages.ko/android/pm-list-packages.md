# pm list packages

> Android 기기에 설치되었거나 알려진 패키지 목록 조회.
> 더 많은 정보: <https://developer.android.com/tools/adb#pm>.

- 설치된 모든 패키지 목록 표시:

`pm list packages`

- 모든 패키지와 해당 APK 파일([f]ile) 경로 표시:

`pm list packages -f`

- 비활성화된([d]isabled) 패키지만 표시:

`pm list packages -d`

- 활성화된([e]nabled) 패키지만 표시:

`pm list packages -e`

- 시스템([s]ystem) 패키지만 표시:

`pm list packages -s`

- 사용자 설치([3]rd-party) 패키지만 표시:

`pm list packages -3`

- 각 패키지의 설치 관리자([i]nstaller) 정보 표시:

`pm list packages -i`

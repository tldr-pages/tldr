# adb shell pm list packages

> Android 기기에서 설치된 패키지, 알려진 패키지 또는 조건에 따라 필터링된 패키지 목록을 출력.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 설치된 모든 패키지 목록 출력:

`adb shell pm list packages`

- 모든 패키지와 해당 APK 파일 경로 출력:

`adb shell pm list packages -f`

- 비활성화된 패키지만 출력:

`adb shell pm list packages -d`

- 활성화된 패키지만 출력:

`adb shell pm list packages -e`

- 시스템 패키지만 출력:

`adb shell pm list packages -s`

- 서드파트(비시스템) 패키지만 출력:

`adb shell pm list packages -3`

- 각 패키지의 설치 프로그램 정보 출력:

`adb shell pm list packages -i`

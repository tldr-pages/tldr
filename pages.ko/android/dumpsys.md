# dumpsys

> Android 시스템 서비스에 대한 제공.
> 이 명령은 `adb shell`을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://developer.android.com/studio/command-line/dumpsys>.

- 모든 시스템 서비스에 대한 진단 출력 가져오기:

`dumpsys`

- 특정 시스템 서비스에 대한 진단 출력 가져오기:

`dumpsys {{서비스}}`

- `dumpsys`가 제공할 수 있는 모든 서비스를 나열:

`dumpsys -l`

- 서비스에 대한 서비스별 인수 나열:

`dumpsys {{서비스}} -h`

- 진단 출력에서 특정 서비스 제외:

`dumpsys --skip {{서비스}}`

- 시간 초과 기간을 초 단위로 지정(기본값은 10초):

`dumpsys -t {{8}}`

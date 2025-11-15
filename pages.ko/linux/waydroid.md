# waydroid

> Ubuntu와 같은 일반적인 Linux 시스템에서 전체 Android 시스템을 부팅하기 위한 컨테이너 기반 접근 방식.
> 더 많은 정보: <https://docs.waydro.id/usage/waydroid-command-line-options>.

- Waydroid 시작:

`waydroid`

- Waydroid 초기화 (최초 실행 시 또는 Android를 재설치한 후 필요):

`sudo waydroid init`

- 파일에서 새로운 Android 앱 설치:

`waydroid app install {{경로/대상/파일.apk}}`

- 패키지 이름으로 Android 앱 실행:

`waydroid app launch {{com.example.app}}`

- Waydroid 세션 시작 또는 중지:

`waydroid session {{start|stop}}`

- Waydroid 컨테이너 관리:

`sudo waydroid container {{start|stop|restart|freeze|unfreeze}}`

- Waydroid 셸 열기:

`sudo waydroid shell`

- Waydroid 창 크기 조정:

`waydroid prop set persist.waydroid.{{width|height}} {{숫자}}`

# automount

> `/etc/auto_master` 파일을 읽고 적절한 마운트 지점에 `autofs`를 마운트하여 디렉터리를 필요에 따라 자동으로 마운트합니다. 본질적으로 시스템의 자동 마운트 프로세스를 수동으로 시작하는 방법입니다.
> 참고: 필요한 권한이 없는 경우 `sudo`로 실행해야 할 수 있습니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/automount.8.html>.

- 자동 마운트를 실행하고, 캐시를 사전에 플러시(`-c`)하고 자세히 출력(`-v`) (가장 일반적인 사용법):

`automount -cv`

- 비활성 상태로 5분(300초) 후 자동으로 마운트 해제:

`automount -t 300`

- automount에 의해 이전에 마운트된 항목 및/또는 `/etc/auto_master`에 정의된 항목 마운트 해제:

`automount -u`

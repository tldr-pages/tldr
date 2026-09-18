# fbset

> 프레임버퍼 장치의 설정을 확인하고 변경.
> 더 많은 정보: <https://manned.org/fbset.1>.

- 현재 프레임버퍼 설정 표시:

`sudo fbset {{[-i|--info]}}`

- `/etc/fb.modes`에 정의된 프레임버퍼 모드 설정:

`sudo fbset "{{800}}x{{600}}-{{60}}"`

- 프레임버퍼의 해상도 설정:

`sudo fbset -xres {{horizontal_픽셀}} -yres {{vertical_픽셀}}`

- 사용자 지정 프레임버퍼 모드 설정:

`sudo fbset {{[-g|--geometry]}} {{tty_가로_해상도}} {{tty_세로_해상도}} {{monitor_가로_해상도}} {{monitor_세로_해상도}} {{색상_깊이}}`

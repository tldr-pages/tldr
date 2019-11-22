# alacritty

> 교차 플랫폼으로, GPU-가속 터미널 에뮬레이터.
> 더 많은 정보: <https://github.com/jwilm/alacritty>.

- 새 alacritty 창 열기:

`alacritty`

- 특정 디렉토리에서 실행:

`alacritty --working-directory {{경로/디렉토리명}}`

- 새로운 alacritty 창에서 명령어 실행:

`alacritty -e {{명령어}}`

- 대체 구성파일 지정 (기본값 : $XDG_CONFIG_HOME/alacritty/alacritty.yml):

`alacritty --config-file {{경로/config.yml}}`

- 재배치가 가능한 라이브 구성 설정으로 실행 (기본적으로 alacritty.yml에서도 활성화 가능):

`alacritty --live-config-reload --config-file {{경로/config.yml}}`

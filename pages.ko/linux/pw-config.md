# pw-config

> PipeWire 서버와 클라이언트에서 사용될 설정 경로와 섹션 나열.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- 사용될 모든 설정 파일 나열:

`pw-config`

- PipeWire PulseAudio 서버에서 사용될 모든 설정 파일 나열:

`pw-config --name pipewire-pulse.conf`

- PipeWire PulseAudio 서버에서 사용되는 모든 설정 섹션 나열:

`pw-config --name pipewire-pulse.conf list`

- JACK 클라이언트에서 사용되는 `context.properties` 조각 나열:

`pw-config --name jack.conf list context.properties`

- JACK 클라이언트에서 사용되는 병합된 `context.properties` 나열:

`pw-config --name jack.conf merge context.properties`

- PipeWire 서버에서 사용되는 병합된 `context.modules` 나열 및 [r]eformat:

`pw-config --name pipewire.conf --recurse merge context.modules`

- 도움말 표시:

`pw-config --help`

# pfetch

> 시스템 정보를 표시.
> 더 많은 정보: <https://github.com/dylanaraps/pfetch>.

- ASCII 아트와 기본 필드 표시:

`pfetch`

- ASCII 아트와 색상 팔레트 필드만 표시:

`PF_INFO="{{ascii palette}}" pfetch`

- 가능한 모든 필드 표시:

`PF_INFO="{{ascii title os host kernel uptime pkgs memory shell editor wm de palette}}" pfetch`

- 다른 사용자 이름과 호스트 이름 표시:

`USER="{{사용자}}" HOSTNAME="{{호스트명}}" pfetch`

- 색상 없이 표시:

`PF_COLOR={{0}} pfetch`

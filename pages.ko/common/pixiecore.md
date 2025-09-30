# pixiecore

> 네트워크 부팅을 관리하는 도구.
> 더 많은 정보: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- `netboot.xyz` 부팅 이미지를 제공하는 PXE 부팅 서버 시작:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Ubuntu 부팅 이미지를 제공하는 새로운 PXE 부팅 서버 시작:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- 빠른 모드에서 사용 가능한 모든 부팅 이미지 나열:

`pixiecore quick --help`

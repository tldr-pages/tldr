# toolbox rmi

> `toolbox` 이미지 제거.
> 같이 보기: `toolbox rm`.
> 더 많은 정보: <https://manned.org/toolbox-rmi.1>.

- 하나 이상의 Toolbx 이미지 제거:

`toolbox rmi {{이미지_이름1 이미지_이름2 ...}}`

- 모든 Toolbx 이미지 제거:

`toolbox rmi --all`

- 현재 컨테이너에서 사용 중인 Toolbx 이미지를 강제로 제거 (컨테이너도 함께 제거됨):

`toolbox rmi --force {{이미지_이름}}`

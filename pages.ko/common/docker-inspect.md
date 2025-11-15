# docker inspect

> Docker 객체에 대한 저수준 정보를 반환.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/inspect/>.

- 도움말 표시:

`docker inspect`

- 이름 또는 ID를 사용하여 컨테이너, 이미지 또는 볼륨에 대한 정보 표시:

`docker inspect {{컨테이너|이미지|ID}}`

- 컨테이너의 IP 주소 표시:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{컨테이너}}`

- 컨테이너의 로그 파일 경로 표시:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{컨테이너}}`

- 컨테이너의 이미지 이름 표시:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{컨테이너}}`

- JSON 형식으로 구성 정보 표시:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{컨테이너}}`

- 모든 포트 바인딩 표시:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{컨테이너}}`

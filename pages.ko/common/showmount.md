# showmount

> NFS 서버의 마운트 정보를 표시.
> 더 많은 정보: <https://manned.org/showmount>.

- 현재 서버에서 마운트 중인 클라이언트를 표시:

`showmount {{호스트명}}`

- NFS 서버의 export 목록을 표시:

`showmount {{[-e|--exports]}} {{호스트명}}`

- 모든 클라이언트와 각 클라이언트가 마운트한 디렉터리를 표시:

`showmount {{[-a|--all]}} {{호스트명}}`

- 클라이언트가 마운트한 디렉터리만 표시:

`showmount {{[-d|--directories]}} {{호스트명}}`

- 헤더 없이 export 목록을 표시:

`showmount {{[-e|--exports]}} --no-headers {{호스트명}}`

- 도움말 표시:

`showmount {{[-h|--help]}}`

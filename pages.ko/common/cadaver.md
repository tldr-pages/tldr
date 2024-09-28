# cadaver

> Unix용 WebDAV 클라이언트.
> 더 많은 정보: <https://manned.org/cadaver>.

- 서버 <dav.example.com>에 연결하고, 루트 컬렉션을 연결:

`cadaver {{http://dav.example.com/}}`

- 특정 포트를 사용하여 서버에 연결하고 `/foo/bar/` 컬렉션을 오픈:

`cadaver {{http://dav.example.com:8022/foo/bar/}}`

- SSL를 사용해 서버에 연결:

`cadaver {{https://davs.example.com/}}`

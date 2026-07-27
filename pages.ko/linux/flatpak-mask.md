# flatpak mask

> 업데이트 및 자동 설치를 제외.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-mask>.

- 지정한 flatpak 애플리케이션의 업데이트 제외:

`flatpak mask {{com.example.app}}`

- 업데이트 제외 해제:

`flatpak mask --remove {{com.example.app}}`

- 현재 제외돈 모든 패턴 목록 표시:

`flatpak mask {{--system|--user}}`

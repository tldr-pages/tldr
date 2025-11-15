# cockpit-desktop

> 실행 중인 세션에서 Cockpit 페이지에 안전하게 접근.
> 격리된 네트워크 공간에서 `cockpit-ws` 및 웹 브라우저를 실행하고, 실행 중인 사용자 세션에서 `cockpit-bridge`를 시작합니다.
> 더 많은 정보: <https://cockpit-project.org/guide/latest/cockpit-desktop.1.html>.

- 페이지 열기:

`cockpit-desktop {{url}} {{SSH_호스트}}`

- 저장소 페이지 열기:

`cockpit-desktop {{/cockpit/@localhost/storage/index.html}}`

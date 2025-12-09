# dockutil

> macOS Dock 항목 관리 도구.
> 더 많은 정보: <https://github.com/kcrawford/dockutil>.

- 현재 사용자 Dock 끝에 애플리케이션 추가:

`dockutil --add {{경로/대상/애플리케이션}}`

- 현재 사용자 Dock에서 한 애플리케이션을 다른 애플리케이션으로 교체:

`dockutil --add {{/경로/대상/애플리케이션}} --replacing '{{dock_item_label}}'`

- 보기 옵션과 함께 폴더를 추가하고 폴더 아이콘 또는 스택으로 표시:

`dockutil --add {{/경로/대상/폴더}} --view {{grid|fan|list|auto}} --display {{folder|stack}}`

- 다른 항목 뒤에 URL Dock 항목 추가:

`dockutil --add {{vnc://example_server.local}} --label '{{Example VNC}}' --after {{dock_item_label}}`

- Dock에서 주어진 Dock 라벨 이름의 애플리케이션 제거:

`dockutil --remove '{{dock_item_label}}'`

- 애플리케이션 뒤에 구분자를 추가:

`dockutil --add '' --type {{spacer|small-spacer|flex-spacer}} --section {{apps}} --after {{dock_item_label}}`

- 모든 구분자 타일 제거:

`dockutil --remove spacer-tiles`

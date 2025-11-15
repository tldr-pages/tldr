# godot

> 오픈 소스 2D 및 3D 게임 엔진.
> 더 많은 정보: <https://docs.godotengine.org/en/latest/tutorials/editor/command_line_tutorial.html>.

- 현재 디렉터리에 `project.godot` 파일이 포함되어 있으면 프로젝트를 실행하고, 그렇지 않으면 프로젝트 관리자를 열기:

`godot`

- 프로젝트 편집 (현재 디렉토리에 `project.godot` 파일이 포함되어 있어야 함):

`godot -e`

- 현재 디렉터리에 `project.godot` 파일이 포함되어 있어도 프로젝트 관리자를 열기:

`godot -p`

- 주어진 내보내기 사전 설정에 대한 프로젝트 내보내기 (사전 설정은 프로젝트에서 정의되어야 함):

`godot --export {{프리셋}} {{출력_경로}}`

- 독립형 GDScript 파일을 실행 (스크립트는 `SceneTree` 또는 `MainLoop`에서 상속되어야 함):

`godot -s {{스크립트.gd}}`

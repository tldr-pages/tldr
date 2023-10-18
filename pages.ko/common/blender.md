# blender

> Blender 3D 컴퓨터 그래픽스 어플리케이션의 커맨드라인 인터페이스. 인자는 주어진 순서대로 실행.
> 더 많은 정보: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- UI를 로드하지 않고 background에서 애니메이션의 모든 프레임을 렌더링.(출력은 `/tmp`에 저장):

`blender -b {{파일명}}.blend -a`

- .blend 파일에 대한 경로 (`//`)에서 특정 이미지 명명 패턴을 사용하여 애니메이션 렌더링:

`blender -b {{파일명}}.blend -o //{{render/frame_###.png}} -a`

- 기존 디렉토리에 저장된 단일 이미지로 애니메이션의 10번째 프레임 렌더링(절대 경로):

`blender -b {{파일명}}.blend -o {{/출력_디렉토리/의/경로}} -f {{10}}`

- 기존 디렉토리에 저장된 JPEG 이미지로 애니메이션의 두번째 마지막 프레임 렌더링(상대 경로):

`blender -b {{파일명}}.blend -o //{{출력_디렉토리}} -F {{JPEG}} -f {{-2}}`

- 프레임 10에서 시작하여 프레임 500에서 끝나는 특정 장면의 애니메이션 렌더링:

`blender -b {{파일명}}.blend -S {{씬_이름}} -s {{10}} -e {{500}} -a`

- Python 표현식을 전달하여 특정 해상도로 애니메이션 렌더링:

`blender -b {{파일명}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' -a`

- Python 콘솔을 사용하여 터미널에서 대화형 Blender 세션 시작(시작 후`import bpy` 수행):

`blender -b --python-console`

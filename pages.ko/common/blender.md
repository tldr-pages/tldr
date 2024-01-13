# blender

> Blender 3D 컴퓨터 그래픽스 어플리케이션의 커맨드라인 인터페이스. 인자는 주어진 순서대로 실행.
> 더 많은 정보: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- UI를 로드하지 않고 background에서 애니메이션의 모든 프레임을 렌더링.(출력은 `/tmp`에 저장):

`blender --background {{파일명}}.blend --render-anim`

- .blend 파일에 대한 경로 (`//`)에서 특정 이미지 명명 패턴을 사용하여 애니메이션 렌더링:

`blender --background {{파일명}}.blend --render-output //{{render/frame_###.png}} --render-anim`

- 기존 디렉토리에 저장된 단일 이미지로 애니메이션의 10번째 프레임 렌더링(절대 경로):

`blender --background {{파일명}}.blend --render-output {{/출력_디렉토리/의/경로}} --render-frame {{10}}`

- 기존 디렉토리에 저장된 JPEG 이미지로 애니메이션의 두번째 마지막 프레임 렌더링(상대 경로):

`blender --background {{파일명}}.blend --render-output //{{출력_디렉토리}} --render-frame {{JPEG}} --render-frame {{-2}}`

- 프레임 10에서 시작하여 프레임 500에서 끝나는 특정 장면의 애니메이션 렌더링:

`blender --background {{파일명}}.blend --scene {{씬_이름}} --frame-start {{10}} --frame-end {{500}} --render-anim`

- Python 표현식을 전달하여 특정 해상도로 애니메이션 렌더링:

`blender --background {{파일명}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' --render-anim`

- Python 콘솔을 사용하여 터미널에서 대화형 Blender 세션 시작(시작 후`import bpy` 수행):

`blender --background --python-console`

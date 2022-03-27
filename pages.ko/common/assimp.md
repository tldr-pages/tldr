# assimp

> Open Asset Import Library 위한 Command-line 클라이언트.
> 40 +3D 파일 형식을 지원하고 몇 개의 유명한 3D포맷으로 내보낼 수 있습니다.
> 더 많은 정보: <http://www.assimp.org/>.

- 지원되는 모든 가져오기 형식을 나열:

`assimp listext`

- 지원되는 모든 내보내기 형식 나열:

`assimp listexport`

- 기본 매개 변수를 사용하여 파일을 지원되는 출력 형식 중 하나로 변환:

`assimp export {{입력_파일명.stl}} {{출력_파일명.obj}}`

- 사용자 정의 매개 변수 (Assimp의 소스 코드 목록에서 dox_cmd.h 파일 사용 가능한 매개 변수)를 사용하여 파일을 변환:

`assimp export {{입력_파일명.stl}} {{출력_파일명.obj}} {{매개변수}}`

- 3D 파일의 내용을 요약하여 표시:

`assimp info {{경로/파일명}}`

- 지원되는 모든 하위 명령 ("Verb")을 나열:

`assimp help`

- 특정 하위 명령에 대한 도움말 얻기 (예 : 특정 하위 명령에 특정 매개 변수):

`assimp {{하위명령어}} --help`

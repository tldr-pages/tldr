# unity

> Unity Editors, 프로젝트 및 모듈을 설치하고 관리하는 도구.
> 더 많은 정보: <https://docs.unity.com/en-us/unity-cli/unity-cli-reference>.

- 지정한 버전의 Unity Editor 설치:

`unity {{[i|install]}} "{{unity_버전}}"`

- Unity 계정에 로그인:

`unity {{[a|auth]}} login`

- 대화형으로 모듈 설치:

`unity {{[im|install-modules]}}`

- 새로운 Universal Render Pipeline 2D 프로젝트 생성:

`unity {{[p|projects]}} new "{{프로젝트_이름}}" --template com.unity.template.universal-2d --path "{{경로/대상/상위_디렉터리}}"`

- 기존 프로젝트 열기:

`unity open "{{경로/대상/프로젝트_디렉터리}}"`

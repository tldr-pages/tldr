# zenity

> 명령줄/셸 스크립트에서 대화 상자를 표시.
> 사용자 입력 값을 반환하거나 오류 시 1을 반환.
> 더 많은 정보: <https://manned.org/zenity>.

- 기본 질문 대화 상자 표시:

`zenity --question`

- "Hello!"라는 텍스트를 표시하는 정보 대화 상자 표시:

`zenity --info --text="{{Hello!}}"`

- 이름/비밀번호 입력 폼을 표시하고 데이터를 ";"로 구분하여 출력:

`zenity --forms --add-entry="{{이름}}" --add-password="{{비밀번호}}" --separator="{{;}}"`

- 사용자가 디렉토리만 선택할 수 있는 파일 선택 폼 표시:

`zenity --file-selection --directory`

- 매초 메시지를 업데이트하고 진행률을 보여주는 진행률 표시줄 표시:

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`

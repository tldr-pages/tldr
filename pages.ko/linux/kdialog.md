# kdialog

> 쉘 스크립트 내에서 KDE 대화 상자를 표시합니다.
> 더 많은 정보: <https://develop.kde.org/docs/administration/kdialog/>.

- 특정 메시지를 표시하는 대화 상자 열기:

`kdialog --msgbox "{{메시지}}" "{{선택_세부_메시지}}"`

- `예`와 `아니오` 버튼이 있는 질문 대화 상자를 열고, 각각 `0`과 `1`을 반환:

`kdialog --yesno "{{메시지}}"`

- `예`, `아니오`, `취소` 버튼이 있는 경고 대화 상자를 열고, 각각 `0`, `1`, 또는 `2`를 반환:

`kdialog --warningyesnocancel "{{메시지}}"`

- 입력 대화 상자를 열고 `확인`을 누를 때 입력을 `stdout`에 출력:

`kdialog --inputbox "{{메시지}}" "{{선택_기본_텍스트}}"`

- 특정 비밀번호를 요청하는 대화 상자를 열고 비밀번호를 `stdout`에 출력:

`kdialog --password "{{메시지}}"`

- 특정 드롭다운 메뉴가 포함된 대화 상자를 열고 선택한 항목을 `stdout`에 출력:

`kdialog --combobox "{{메시지}}" "{{항목1}}" "{{항목2}}" "{{...}}"`

- 파일 선택 대화 상자를 열고 선택한 파일의 경로를 `stdout`에 출력:

`kdialog --getopenfilename`

- 진행 표시줄 대화 상자를 열고 통신을 위한 D-Bus 참조를 `stdout`에 출력:

`kdialog --progressbar "{{메시지}}"`

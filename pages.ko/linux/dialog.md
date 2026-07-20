# dialog

> 터미널에 대화상자를 표시.
> 관련 항목: `gum`, `whiptail`.
> 더 많은 정보: <https://manned.org/dialog>.

- 메시지 표시:

`dialog --msgbox "{{Message}}" {{높이}} {{너비}}`

- 사용자에게 텍스트 입력 요청:

`dialog --inputbox "{{Enter text:}}" {{8}} {{40}} 2>{{출력파일.txt}}`

- 사용자에게 예/아니오 확인 요청:

`dialog --yesno "{{Continue?}}" {{7}} {{40}}`

- 도움말 표시:

`dialog`

# kwriteconfig5

> KDE Plasma의 KConfig 항목 쓰기.
> 더 많은 정보: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- 도움말 표시:

`kwriteconfig5 --help`

- 전역 설정 키 설정:

`kwriteconfig5 --group {{그룹_이름}} --key {{키}} {{값}}`

- 특정 설정 파일에 키 설정:

`kwriteconfig5 --file {{경로/대상/파일}} --group {{그룹_이름}} --key {{키}} {{값}}`

- 키 삭제:

`kwriteconfig5 --group {{그룹_이름}} --key {{키}} --delete`

- systemd를 사용하여 Plasma 세션이 가능할 때 시작:

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}} {{true}}`

- 창이 최대화될 때 제목 표시줄 숨기기 (Ubuntu와 유사):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- KRunner를 Meta(커맨드/윈도우) 글로벌 핫키로 열리도록 설정:

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} "{{org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch}}"`

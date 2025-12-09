# qdbus

> Inter-Process Communication (IPC) 및 Remote Procedure Calling (RPC) 메커니즘으로, 원래 Linux를 위해 개발되었습니다.
> 더 많은 정보: <https://doc.qt.io/qt-5/qtdbus-index.html>.

- 사용 가능한 서비스 이름 나열:

`qdbus`

- 특정 서비스의 객체 경로 나열:

`qdbus {{서비스_이름}}`

- 특정 객체에서 사용 가능한 메서드, 신호 및 속성 나열:

`qdbus {{서비스_이름}} {{/대상/경로/객체}}`

- 인수를 전달하여 특정 메서드를 실행하고 반환된 값 표시:

`qdbus {{서비스_이름}} {{/대상/경로/객체}} {{메서드_이름}} {{인수1}} {{인수2}}`

- KDE Plasma 세션에서 현재 밝기 값 표시:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- KDE Plasma 세션에서 특정 밝기 설정:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- KDE Plasma 세션에서 볼륨 증가 단축키 호출:

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- 정상적으로 로그아웃한 후 아무것도 하지 않거나, 재부팅하거나, 종료:

`qdbus {{org.kde.Shutdown}} {{/Shutdown}} {{logout|logoutAndReboot|logoutAndShutdown}}`

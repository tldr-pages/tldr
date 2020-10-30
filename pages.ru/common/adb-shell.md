# adb shell

> Android Debug Bridge Shell: ������ �������� ��������� �������� �� ��������� Android ��� ������������ ���������� Android.
> ������ ����������: <https://developer.android.com/studio/command-line/adb>.

- ��������� �������� ������������� �������� �� ���������/����������:

`adb shell`

- �������� ��� �������� �� ��������� ��� ����������:

`adb shell getprop`

- ������� ���� ����������� �������� �� ���������:

`adb shell pm reset-permissions`

- �������� ������� ���������� ��� ����������:

`adb shell pm revoke {{�����}} {{����������}}`

- ��������� �������� �������:

`adb shell input keyevent {{keycode}}`

- �������� ������ ���������� �� ��������� ��� ����������:

`adb shell pm clear {{�����}}`

- ��������� activity �� ���������/����������:

`adb shell am start -n {{�����}}/{{activity}}`

- ��������� ������� activity �� ��������� ��� ����������:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`

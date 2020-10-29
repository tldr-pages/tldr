# adb reverse

> Android Debug Bridge Reverse: �������� ���������� �� ��������� Android ��� ������������� ���������� Android.
> ������ ����������: <https://developer.android.com/studio/command-line/adb>.

- ������� ������ ���� �������� ���������� �� ���������� � ���������:

`adb reverse --list`

- ������� TCP-���� �� ��������� ��� ���������� �� localhost:

`adb reverse tcp:{{��������_����}} tcp:{{���������_����}}`

- ������� �������� ���������� �� ��������� ��� ����������:

`adb reverse --remove tcp:{{��������_����}}`

- ������� ��� �������� ���������� �� ���� ���������� � �����������:

`adb reverse --remove-all`

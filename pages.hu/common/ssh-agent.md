# ssh-agent

> Egy SSH-ügynök folyamat indítása.
> Az SSH-ügynök a memóriában tárolja a dekódolt SSH-kulcsokat, amíg el nem távolítják, vagy a folyamatot meg nem ölik.
> Lásd még: `ssh-add`, amely az SSH-ügynök által tárolt kulcsokat hozzáadhatja és kezelheti.
> További információ: <https://man.openbsd.org/ssh-agent>.

- SSH-ügynök indítása az aktuális héjhoz:

`eval $(ssh-agent)`

- Az éppen futó ügynök megállítása:

`ssh-agent -k`

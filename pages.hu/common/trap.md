# trap

> Automatikusan végrehajtja a parancsokat, miután a folyamatok vagy az operációs rendszer jeleket kapott. Használható a felhasználó megszakításai vagy más műveletek miatti takarítások elvégzésére. További információ: <https://manned.org/trap>.

- Listázza a rendelkezésre álló jeleket, amelyekre csapdákat lehet beállítani:

`trap -l`

- Az aktuális héj aktív csapdáinak listázása:

`trap -p`

- Csapda beállítása egy vagy több jel észlelésekor parancsok végrehajtásához:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Aktív csapdák eltávolítása:

`trap - {{SIGHUP}} {{SIGINT}}`

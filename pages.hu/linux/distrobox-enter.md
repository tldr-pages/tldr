# distrobox-enter

> Egy parancs futtatása egy Distrobox konténerben.
> Az alapértelmezett végrehajtott parancs a SHELL, de megadhat különböző héjakat vagy teljes parancsokat is.
> Ha egy szkriptben, alkalmazásban vagy szolgáltatásban használod, megadhatod a --headless módot a tty és az interaktivitás kikapcsolásához.
> További információ: <https://distrobox.privatedns.org>.

- Lépjen be egy disztribúcióba, és futtassa a `sh -l`:

`distrobox-enter container-name -- sh -l`

- Belépés egy distroboxba anélkül, hogy tty-t instanciázna:

`distrobox-enter -H container-name -- uptime -p`

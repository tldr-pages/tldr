# launchctl

> Parancssori interfész az Apple `launchd` kezelőjéhez a démonok (rendszerszintű szolgáltatások) és a launch agentek (felhasználókra szabott programok) indításához.
> `launchd` betölti a megfelelő helyeken elhelyezett XML-alapú `*.plist` fájlokat, és a megfelelő parancsokat a meghatározott ütemezés szerint futtatja.
> További információ: <https://manned.org/launchctl>.

- Aktiváljon egy felhasználó-specifikus ügynököt, amely a felhasználó bejelentkezésekor betöltődik a `launchd` oldalra:

`launchctl load ~/Library/LaunchAgents/{{my_script}}.plist`

- Aktiváljon egy olyan ügynököt, amelynek futtatásához root jogosultságok szükségesek, és/vagy amelyet bármely felhasználó bejelentkezésekor be kell tölteni (vegye figyelembe, hogy az elérési útvonalból hiányzik a `~` ):

`sudo launchctl load /Library/LaunchAgents/{{root_script}}.plist`

- Aktiváljon egy rendszerszintű démont, amely a rendszer indításakor betöltődik (még akkor is, ha egyetlen felhasználó sem lép be):

`sudo launchctl load /Library/LaunchDaemons/{{system_daemon}}.plist`

- Az összes betöltött ügynök/daemon megjelenítése, a PID-vel, ha az általuk megadott folyamat jelenleg fut, és a legutóbbi futtatáskor visszaadott kilépési kóddal:

`launchctl list`

- Egy aktuálisan betöltött ügynök kitöltésének megszüntetése, pl. módosítások elvégzése céljából (megjegyzés: a plist fájl automatikusan betöltődik a `launchd` címre újraindítás és/vagy bejelentkezés után):

`launchctl unload ~/Library/LaunchAgents/{{my_script}}.plist`

- Egy ismert (betöltött) ágens/daemon kézi futtatása, még akkor is, ha nem a megfelelő időpontban van (megjegyzés: ez a parancs az ágens címkéjét használja, nem pedig a fájlnevet):

`launchctl start {{my_script}}`

- Manuálisan megölheti az ismert ügynökhöz/démonhoz kapcsolódó folyamatot, ha az fut:

`launchctl stop {{my_script}}`

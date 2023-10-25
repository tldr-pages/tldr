# launchctl

> Beheer Apple's `launchd` manager voor launch daemons (systeembrede diensten) en launch agents (programma's per gebruiker).
> `launchd` laadt op XML gebaseerde `*.plist`-bestanden die op de juiste locaties zijn geplaatst, en voert de corresponderende commando's uit volgens hun gedefinieerde schema.
> Meer informatie: <https://manned.org/launchctl>.

- Activeer een gebruikersspecifieke agent die in `launchd` moet worden geladen wanneer de gebruiker inlogt:

`launchctl load ~/Library/LaunchAgents/{{my_script}}.plist`

- Activeer een agent die root-rechten vereist om te kunnen werken en/of moet worden geladen wanneer een gebruiker inlogt (let op de afwezigheid van `~` in het pad):

`sudo launchctl load /Library/LaunchAgents/{{root_script}}.plist`

- Activeer een systeembrede daemon die moet worden geladen wanneer het systeem opstart (zelfs als er geen gebruiker inlogt):

`sudo launchctl load /Library/LaunchDaemons/{{system_daemon}}.plist`

- Toon alle geladen agenten/daemons, met de PID als het proces dat ze specificeren momenteel actief is, en de afsluitcode de laatste keer dat ze werden uitgevoerd terugstuurde:

`launchctl list`

- Een momenteel geladen agent ontladen, b.v. om wijzigingen aan te brengen (let op: het plist-bestand wordt automatisch in `launchd` geladen na een herstart en/of inloggen):

`launchctl unload ~/Library/LaunchAgents/{{my_script}}.plist`

- Voer handmatig een bekende (geladen) agent/daemon uit, zelfs als dit niet het juiste moment is (opmerking: deze opdracht gebruikt het label van de agent, in plaats van de bestandsnaam):

`launchctl start {{script_bestand}}`

- Beëindig handmatig het proces dat is gekoppeld aan een bekende agent/daemon, als deze actief is:

`launchctl stop {{script_bestand}}`

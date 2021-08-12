# nethogs

> Monitorizați utilizarea lățimii de bandă pentru fiecare proces.
> Mai multe informaţii: <https://github.com/raboof/nethogs>

- Porniți nethogs ca root (dispozitivul implicit este eth0):

`sudo nethogs`

- Monitorizarea lățimii de bandă pe un anumit dispozitiv:

`sudo nethogs {{device}}`

- Monitor lățime de bandă pe mai multe dispozitive:

`sudo nethogs {{device1}} {{device2}}`

- Specificați rata de împrospătare:

`sudo nethogs -t {{seconds}}`

# chcon

> Verander SELinux beveiligingscontext van een bestand of bestanden/mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/chcon>.

- Toon beveiligingscontext van een bestand:

`ls -lZ {{pad/naar/bestand}}`

- Verander de beveiligingscontext van een doelbestand, door gebruik te maken van een referentiebestand:

`chcon --reference={{referentiebestand}} {{doelbestand}}`

- Verander de volledige SELinux beveiligingscontext van een bestand:

`chcon {{gebruiker}}:{{rol}}:{{type}}:{{bereik/niveau}} {{bestandsnaam}}`

- Verander alleen het gebruikersgedeelte van de SELinux beveiligingscontext:

`chcon -u {{user}} {{bestandsnaam}}`

- Verander alleen het rolgedeelte van de SELinux beveiligingscontext:

`chcon -r {{rol}} {{bestandsnaam}}`

- Verander alleen het typegedeelte van de SELinux beveiligingscontext:

`chcon -t {{type}} {{bestandsnaam}}`

- Verander alleen het bereik/niveaugedeelte van de SELinux beveiligingscontext:

`chcon -l {{bereik/niveau}} {{bestandsnaam}}`

# velero

> Copierea de rezervă și migrarea aplicațiilor Kubernetes și volumele lor persistente.
> Mai multe informaţii: <https://github.com/heptio/velero>

- Creați o copie de rezervă care conține toate resursele:

`velero backup create {{backup_name}}`

- Listează toate copiile de rezervă:

`velero backup get`

- Ștergeți o copie de rezervă:

`velero backup delete {{backup_name}}`

- Creați o copie de rezervă săptămânală, fiecare trăind timp de 90 de zile (2160 ore):

`velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- Creați o restaurare din cea mai recentă copie de rezervă de succes declanșată de un anumit program:

`velero restore create --from-schedule {{schedule_name}}`

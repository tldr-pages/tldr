# chattr

> Modificați atributele fișierelor sau directoarelor.
> Mai multe informaţii: <https://manned.org/chattr>

- Faceți un fișier sau un director imuabil modificărilor și ștergerii, chiar și de către superuser:

`chattr +i {{path/to/file_or_directory}}`

- Faceți un fișier sau un director mutabil:

`chattr -i {{path/to/file_or_directory}}`

- Recursiv face un întreg director și conținut imuabil:

`chattr -R +i {{path/to/directory}}`

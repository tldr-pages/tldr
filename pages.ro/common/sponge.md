# sponge

> Bucurați-vă de intrare înainte de a scrie fișierul de ieșire.
> Mai multe informaţii: <https://manned.org/sponge>

- Adăugarea conținutului fișierului la fișierul sursă:

`cat {{path/to/file}} | sponge -a {{path/to/file}}`

- Eliminați toate liniile începând cu # într-un fișier:

`grep -v '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}`

# k8sec

> instrument de interfață linie de comandă pentru a gestiona secretele Kubernetes.
> Mai multe informaţii: <https://github.com/dtan4/k8sec>

- Listează toate secretele:

`k8sec list`

- Listează un secret specific ca un șir codificat base64-bază:

`k8sec list {{secret_name}} --base64`

- Stabileşte valoarea unui secret:

`k8sec set {{secret_name}} {{key=value}}`

- Setați o valoare codificată de bază 64:

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- Desenează un secret:

`k8sec unset {{secret_name}}`

- Încărcați secrete dintr-un fișier:

`k8sec load -f {{path/to/file}} {{secret_name}}`

- Dump secrete într-un fișier:

`k8sec dump -f {{path/to/file}} {{secret_name}}`

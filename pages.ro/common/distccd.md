# distccd

> Demon server pentru compilatorul distribuit distcc.
> Mai multe informaţii: <https://distcc.github.io>

- Porniți un daemon cu setările implicite:

`distccd --daemon`

- Porniți un daemon, acceptați conexiuni din intervalele de rețea privată IPv4:

`distccd --daemon --allow-private`

- Porniți un daemon, acceptând conexiuni de la o anumită adresă de rețea sau interval de adrese:

`distccd --daemon --allow {{ip_address|network_prefix}}`

- Porniți un daemon cu o prioritate redusă, care poate executa maximum 4 sarcini simultan:

`distccd --daemon --jobs {{4}} --nice {{5}}`

- Porniți un daemon și înregistrați-l prin MDNS/DNS-SD (Zeroconf):

`distccd --daemon --zeroconf`

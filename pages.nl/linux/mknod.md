# mknod

> Maak speciale bestanden voor blok- of tekenapparaten aan.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- Maak een blokapparaat aan:

`sudo mknod {{pad/naar/apparaat_bestand}} b {{groot_apparaatnummer}} {{klein_apparaatnummer}}`

- Maak een tekenapparaat aan:

`sudo mknod {{pad/naar/apparaat_bestand}} c {{groot_apparaatnummer}} {{klein_apparaatnummer}}`

- Maak een FIFO (queue) apparaat aan:

`sudo mknod {{pad/naar/apparaat_bestand}} p`

- Maak een apparaatbestand aan met de standaard SELinux-beveiligingscontext:

`sudo mknod {{[-Z|--context]}} {{pad/naar/apparaat_bestand}} {{type}} {{groot_apparaatnummer}} {{klein_apparaatnummer}}`

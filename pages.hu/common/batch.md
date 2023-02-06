# batch

> A parancsok végrehajtása egy későbbi időpontban, amikor a rendszer terhelési szintje lehetővé teszi. Az atd (vagy atrun) szolgáltatásnak futnia kell a tényleges végrehajtásokhoz. További információ: <https://manned.org/batch>.

- Parancsok végrehajtása a standard bemenetről (nyomja meg a `Ctrl + D` gombot, ha kész):

`batch`

- Parancsok végrehajtása a standard bemenetről:

`echo "{{./make_db_backup.sh}}" | batch`

- Parancsok végrehajtása egy adott fájlból:

`batch -f {{path/to/file}}`

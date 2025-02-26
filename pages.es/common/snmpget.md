# snmpget

> Consulta utilizando el protocolo SNMP.
> Más información: <https://manned.org/snmpget>.

- Solicita un único valor al agente SNMP:

`snmpget -v {{versión}} -c {{comunidad}} {{ip}} {{oid}}`

- Muestra la ruta completa del identificador de objeto (OID):

`snmpget -v {{versión}} -c {{comunidad}} -O f {{ip}} {{oid}}`

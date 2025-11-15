# modetest

> Diagnose Direct Rendering Manager and Kernel Mode Setting.
> More information: <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841850/Video_Mixer#modetest>.

- List connectors and their available modes for a specific driver:

`modetest -M {{mgag200}} -c`

- Set the resolution of a connector:

`sudo modetest -M {{mgag200}} -s {{connector_id}}:{{1600}}x{{1200}}`

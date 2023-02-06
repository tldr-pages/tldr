# avahi-browse

> Megjeleníti a helyi hálózaton mDNS/DNS-SD-n keresztül elérhető szolgáltatásokat és állomáshelyeket. Az Avahi kompatibilis az Apple eszközökben található Bonjourral (Zeroconf). További információ: <https://www.avahi.org/>.

- A helyi hálózaton elérhető összes szolgáltatás listázása címükkel és portjaikkal együtt, miközben a helyi szolgáltatásokat figyelmen kívül hagyja:

`avahi-browse --all --resolve --ignore-local`

- Listázza az összes tartományt:

`avahi-browse --browse-domains`

- A keresést egy adott tartományra korlátozza:

`avahi-browse --all --domain={{domain}}`

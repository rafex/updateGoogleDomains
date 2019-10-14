# updateDuckDNS
Actualiza la IP de Duck DNS para que siempre esté actualizada en un servidor GNU/Linux de IP dinámica.

Se sugiere que la carpeta esté dentro de “/opt”, sin embargo puede modificar esta ruta en el archivo "updateDuckDNS" en la siguiente variable:

```Shell
#!/bin/bash

PATH_INSTALL_SCRIPT_PYTHON="/opt/updateDuckDNS"
```
Puede que requiera permisos especiales para crear la carpeta de logs en "/var/log"

Para instalar las dependencias del script de python requiere tener instalado python3 y pip3, si satisface estas dependencias podrá usar el siguiente comando:

```Shell
pip install -r requirements.txt
```
Habrá que agregar una línea al "crontab", se sugiere que sea cada 5 minutos pero puede ajustar este tiempo a su conveniencia, así como colocar el usuario que desea que ejecute este proceso, se recomienda que no sea "root":

```Shell
*/5 * * * *     <USER>   /opt/updateDuckDNS/updateDuckDNS
```

Debe modifcar las variables del archivo "updateDuckDNS"

```Shell
export UPDATE_DUCK_DNS_TOKEN=<aquí va el token que se genera en la página de duckdns.org>
export UPDATE_DUCK_DNS_SUB_DOMAIN=<el nombre del subdominio creado en duckdns.org>
```

Puedes leerme en: [https://theworldofrafex.blog/](https://theworldofrafex.blog/)


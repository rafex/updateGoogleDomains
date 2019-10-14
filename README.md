# updateDuckDNS
Actualiza la IP de Google Domains para que siempre esté actualizada en un servidor GNU/Linux de IP dinámica.

Se sugiere que la carpeta esté dentro de “/opt”, sin embargo puede modificar esta ruta en el archivo "updateGoogleDomains" en la siguiente variable:

```Shell
#!/bin/bash

PATH_INSTALL_SCRIPT_PYTHON="/opt/updateGoogleDomains"
```
Puede que requiera permisos especiales para crear la carpeta de logs en "/var/log"

Para instalar las dependencias del script de python requiere tener instalado python3 y pip3, si satisface estas dependencias podrá usar el siguiente comando:

```Shell
pip install -r requirements.txt
```
Habrá que agregar una línea al "crontab", se sugiere que sea cada 5 minutos pero puede ajustar este tiempo a su conveniencia, así como colocar el usuario que desea que ejecute este proceso, se recomienda que no sea "root":

```Shell
*/5 * * * *     <USER>   /opt/updateGoogleDomains/updateGoogleDomains
```

Debe modifcar las variables del archivo "updateGoogleDomains"

```Shell
export UPDATE_GOOGLE_DOMAINS_USER=<el user que esta en el panel de Google Domains en DNS dinámico>
export UPDATE_GOOGLE_DOMAINS_PASS=<el password que esta en el panel de Google Domains en DNS dinámico>
export UPDATE_GOOGLE_DOMAINS_DOMAIN=<el dominio que se compro en Google Domains>
export UPDATE_GOOGLE_DOMAINS_SUB_DOMAIN=<el subdominio por ejemplo www o si es la raíz es @>
```

Puedes leerme en: [https://theworldofrafex.blog/](https://theworldofrafex.blog/)


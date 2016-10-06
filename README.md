# wikanda

Scripts para los wikis de [Wikanda](https://www.wikanda.es)

* **crea-redirecciones.py**: Crea páginas de redirección sin acentos y sin importar mayúsculas/minúsculas. De este modo si alguien escribe "[Sanlucar de Barrameda](https://cadizpedia.wikanda.es/wiki/Sanlucar_de_Barrameda)" en el buscador de Cadizpedia (y se le olvida el acento en la u), el wiki le redireccionaría automáticamente al artículo "Sanlúcar de Barrameda", lo que mejora la usabilidad del sitio. Y así con miles de títulos que contengan acentos.
* **crea-red-municipios.py**: Crea redirecciones a todos los municipios de Andalucía en el wiki global Wikanda, apuntando hacia las locapedias. [Ver ejemplo](https://www.wikanda.es/wiki/Villanueva_del_Ariscal).
* **sube-wikia-dumps-ia.py**: Sube una [copia de los dumps](https://dumps.wikanda.es) a [Internet Archive](https://archive.org/search.php?query=almeriapedia%20OR%20cadizpedia%20OR%20cordobapedia%20OR%20granadapedia%20OR%20huelvapedia%20OR%20jaenpedia%20OR%20malagapedia%20OR%20sevillapedia%20OR%20wikanda) para su preservación.

Ficheros de configuración:

* **user-config.py**: para la configuración del usuario bot.
* **wikanda_family.py**: para configurar el acceso a las pedias.

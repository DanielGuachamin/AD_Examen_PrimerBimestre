# AD_Examen_PrimerBimestre

El script 1 usa los keys y tokens generados mediante la cuente developer de twitter e importa varias librerias para
que funcione adecuadamente la conexion con couchDB y las funciones de la API de twitter.

Para este ejercicio se uso la ubicacion de 3 ciudades diferentes:
Guadalajara
https://raw.githubusercontent.com/DanielGuachamin/Contador_de_palabras_desde_un_archivo_txt/master/Ciudad1_Guadalajara.PNG
Acapulco
https://raw.githubusercontent.com/DanielGuachamin/Contador_de_palabras_desde_un_archivo_txt/master/Ciudad2_Acapulco.PNG
Chone
https://raw.githubusercontent.com/DanielGuachamin/Contador_de_palabras_desde_un_archivo_txt/master/Ciudad2_Chone.PNG
A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/Capturas/EjecucionCorrecta_Script1.PNG
Esto tambien puede comprobarse mediante la captura de CouchDB:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/CouchDB_BDciudades.PNG

El script 2 usa los keys y tokens generados mediante la cuente developer de twitter e importa varias librerias para
que funcione adecuadamente la conexion con couchDB y las funciones de la API de twitter.

Para este ejercicio se uso el termino clave (track) 'juegos olimpicos':
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/EjecucionCorrecta_Script2.PNG

Esto tambien puede comprobarse mediante la captura de CouchDB:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/CouchDB_BDolimpicos.PNG

El script 3 enfocado en el webscrapign se uso una pagina que daba noticias sobre los juegos olimpicos, donde se
filtro el codigo html mediante etiquetas y clases para finalmente formar el json y pasarlo a mongodb
A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/EjecucionCorrecta_Script3.PNG

Esto tambien puede comprobarse mediante la captura de mongoDB:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/MongoDB_BDolimpicos.PNG

El script 4 utiliza una libreria de facebook scraper la cual se encargara de recopilar información importante
dentro de un json con base en un nombre de referencia. Este va formando el json el cual será guardado en una base de datos
de mongodb mediante python y la funcion insert_one()

A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/EjecucionCorrecta_Script4.PNG

Esto tambien puede comprobarse mediante la captura de mongoDB:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/MongoDB_BDolimpicosfacebook.PNG

El script 5 se ejecuto mediante la terminal git bash para hacer uso de tik-tok-scraper lo cual sirvio para descargar
en formato json dos fuente relacionadas a los juegos olimpicos asi:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/Fuentes_TikTok.PNG

Despues se uso el script 5 para leer el json generado y pasarlo a SQLite. A continuación se presentan las imágenes 
que confirman el funcionamiento adecuado de este script:
https://raw.githubusercontent.com/DanielGuachamin/AD_Examen_PrimerBimestre/master/SQLite_Tableolimpicos.PNG


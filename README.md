# AD_Examen_PrimerBimestre

El script 1 usa los keys y tokens generados mediante la cuente developer de twitter e importa varias librerias para
que funcione adecuadamente la conexion con couchDB y las funciones de la API de twitter.

Para este ejercicio se uso la ubicacion de 3 ciudades diferentes:
Guadalajara
![Ciudad1_Guadalajara](https://user-images.githubusercontent.com/66534512/127725268-d8a0a49d-3193-4af8-b73f-7d1d41c992a1.PNG)
Acapulco
![Ciudad2_Acapulco](https://user-images.githubusercontent.com/66534512/127725286-fcd7d49e-8d4b-4c9f-84fa-9c811dc1616e.PNG)
Chone
![Ciudad3_Chone](https://user-images.githubusercontent.com/66534512/127725290-c7422c0a-3d1a-41b4-a8f5-1ff26d119bba.PNG)
A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
![EjecucionCorrecta_Script1](https://user-images.githubusercontent.com/66534512/127725295-2447c25d-0f22-4134-a0af-ddac90314ffd.PNG)
Esto tambien puede comprobarse mediante la captura de CouchDB:
![CouchDB_BDciudades](https://user-images.githubusercontent.com/66534512/127725298-0ada374c-91a3-4fa2-b789-3cf36d8b8dd2.PNG)

El script 2 usa los keys y tokens generados mediante la cuente developer de twitter e importa varias librerias para
que funcione adecuadamente la conexion con couchDB y las funciones de la API de twitter.

Para este ejercicio se uso el termino clave (track) 'juegos olimpicos':
![EjecucionCorrecta_Script2](https://user-images.githubusercontent.com/66534512/127725300-d6990f7d-04e6-4b14-a846-4ae1eacd6db5.PNG)

Esto tambien puede comprobarse mediante la captura de CouchDB:
![CouchDB_BDolimpicos](https://user-images.githubusercontent.com/66534512/127725307-2b4bc627-c3a9-442c-9754-169c9da074c6.PNG)

El script 3 enfocado en el webscrapign se uso una pagina que daba noticias sobre los juegos olimpicos, donde se
filtro el codigo html mediante etiquetas y clases para finalmente formar el json y pasarlo a mongodb
A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
![EjecucionCorrecta_Script3](https://user-images.githubusercontent.com/66534512/127725316-13954d21-d8da-4bcb-a2b9-89ce686e20d9.PNG)

Esto tambien puede comprobarse mediante la captura de mongoDB:
![MongoDB_BDolimpicos](https://user-images.githubusercontent.com/66534512/127725325-a63f92d7-9f20-459b-ad2f-c9cdaa9aa374.PNG)

El script 4 utiliza una libreria de facebook scraper la cual se encargara de recopilar información importante
dentro de un json con base en un nombre de referencia. Este va formando el json el cual será guardado en una base de datos
de mongodb mediante python y la funcion insert_one()

A continuación se presentan las imágenes que confirman el funcionamiento adecuado de este script:
![EjecucionCorrecta_Script4](https://user-images.githubusercontent.com/66534512/127725332-276bffd0-ebe9-4652-9d88-597d0b7d3637.PNG)

Esto tambien puede comprobarse mediante la captura de mongoDB:
![MongoDB_BDolimpicosfacebook](https://user-images.githubusercontent.com/66534512/127725335-b1414d69-ced8-4ea9-b627-c1c03ca165ac.PNG)

El script 5 se ejecuto mediante la terminal git bash para hacer uso de tik-tok-scraper lo cual sirvio para descargar
en formato json dos fuente relacionadas a los juegos olimpicos asi:
![Fuentes_TikTok](https://user-images.githubusercontent.com/66534512/127725346-ea898d00-b2a6-4c82-824d-2a793954a2ed.PNG)

Despues se uso el script 5 para leer el json generado y pasarlo a SQLite. A continuación se presentan las imágenes 
que confirman el funcionamiento adecuado de este script:
![SQLite_Tableolimpicos](https://user-images.githubusercontent.com/66534512/127725349-3b59997f-8ba5-4e7e-ba59-d69e6632500c.PNG)


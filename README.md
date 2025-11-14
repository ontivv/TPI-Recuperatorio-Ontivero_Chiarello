# TRABAJO PRACTICO INTEGRADOR: Recuperatorio 
## Santiago Ontivero - Joaquín Chiarello

## DESCRIPCIÓN DEL PROGRAMA:
El programa en cuestión se basa en la idea de mediante el uso de un archivo CSV denominado "paises.csv" se analicen la información brindada por la base de datos del mismo y se puedan realizar acciones tales como:

- Busqueda de datos específicos por NOMBRE DEL PAÍS
- Filtrado de países por: CONTINENTE , POBLACIÓN y SUPERFICIE
- Impresión de países ordenados por: NOMBRE , SUPERFICIE y POBLACIÓN
- Impresión de datos estadísticos como: PAÍS CON MENOR POBLACIÓN , PAÍS CON MAYOR POBLACIÓN , PROMEDIO DE POBLACIÓN DE PAÍSES y PROMEDIO DE SUPERFICIE DE PAÍSES

## ARCHIVOS

### crud.py:
Uno de los archivos más importantes de todo el programa. El codigo de este progrma es un módulo para gestionar los datos de un archivo paises.csv. Define un conjunto de funciones para realizar las operaciones básicas de CRUD sobre ese archivo. Este se encarga de la persistencia de datos, se asegura de que la información de los países se pueda guardar en el disco para no perderla cuando se cierra el programa, y se pueda leer de nuevo cuando el programa se abre.

#### ¿Cómo logra esto?
El archivo lo logra gestionando la entrada y salida de datos. Se encarga de leer el archivo paises.csv para convertir sus datos de texto en una lista de diccionarios que el programa pueda usar en memoria. A la inversa, toma esa lista de diccionarios de la memoria (con los cambios del usuario) y la escribe de nuevo en el archivo "paises.csv" en el disco. Estas operaciones de lectura y escritura están organizadas en sus diferentes funciones.


------------------------------------------------------------------


### validaciones.py
Es el modulo de seguridad del programa. Su único propósito es proteger al sistema contra datos incorrectos o inválidos que el usuario intente ingresar. Cumple con la robustez que necesita el programa para funcionar correctamente ya que se asegura de que el programa no se "rompa" (no crashee) si el usuario escribe letras donde van números, o si deja un campo importante vacío. También ayuda a mantener la integridad de los datos (ej: no permite poblaciones negativas).

#### ¿Cómo logra esto?
El archivo lo logra utilizando diversas funciones para evitar que el programa se rompa o termine abruptamente por un error de escritura del usuario.


------------------------------------------------------------------


### estadistica.py
es el módulo de análisis del programa. Su propósito no es guardar ni modificar datos, sino tomar los datos existentes y generar información útil a partir de ellos. Se encarga del procesamiento y reporte de datos. Transforma la "base de datos" (la lista de países) en respuestas concretas a preguntas específicas (cuál es el promedio, cuál es el mayor, etc.), proporcionando valor al usuario más allá de solo almacenar la información.

#### ¿Cómo logra esto?
El archivo logra esto combinando funciones de cálculo (que hacen la matemática) con funciones de interfaz (que manejan el menú de esta sección).


------------------------------------------------------------------


### filtrar_paises.py
Este módulo filtra la lista completa de países según criterios específicos (continente, población, etc.) e imprime los resultados en pantalla. No modifica los datos, solo los muestra. Cada función se encarga de un tipo de filtro.

#### ¿Cómo logra eso?
Este módulo recorre la lista completa de países con un bucle for. Dentro del bucle, comprueba cada país con una condición if para ver si coincide con el criterio de búsqueda (ej. pais["continente"] == "america"). Si coincide, imprime la información de ese país en la consola.


------------------------------------------------------------------

### ordenamiento.py
Este modulo realiza la visualización ordenada de datos. Su propósito es tomar la lista completa de países y mostrarla en la consola organizada por un criterio específico: alfabéticamente por nombre, o en orden numérico (de menor a mayor) por población o superficie. Este módulo no modifica la lista original, solo la lee y la presenta de una forma diferente, e incluye el submenú para que el usuario elija cómo verla.

#### ¿Cómo logra esto?
Para hacerlo primero extrae solo la columna de datos a ordenar (ej: todas las poblaciones) a una nueva lista temporal. Luego, ordena esa lista temporal usando la función sorted(). Finalmente, itera sobre esa lista ya ordenada y, por cada valor, vuelve a recorrer la lista de países original para encontrar el diccionario completo que coincide con esa condición e imprimir sus detalles.

------------------------------------------------------------------

### buscarnombre.py
Este modulo realiza la búsqueda y recuperación de un dato específico. Su único propósito es encontrar un país dentro de la lista principal basándose en su nombre, y devolver el diccionario completo de ese país (con su población, superficie, etc.) al programa principal.

#### ¿Cómo logra esto?
Para hacerlo, la función buscar_pais recorre la lista completa de países con un bucle for. En cada iteración, comprueba con un if si el nombre_pais que se está buscando es exactamente igual al valor de la clave "nombre" del país actual. Si encuentra una coincidencia, detiene la búsqueda inmediatamente y retorna el diccionario completo (pais). Si el bucle for termina sin encontrar nada, retorna un mensaje de error.


------------------------------------------------------------------


### principal.py
Este modulo es el archivo main de todo el programa, es el corazon del mismo. Es el punto de entrada y el "orquestador" de toda la aplicación. Su propósito es integrar todos los demás modulos (crud, validaciones, filtrar_paises, etc.) y presentarlos al usuario a través de un menú interactivo. Es el "cerebro" que gestiona la navegación del usuario y también contiene la fuente de datos base (la lista en paises_en_lista) que se utiliza para todas las operaciones.

Para hacerlo, la función principal() primero se asegura de que el archivo CSV exista usando la lista de datos base. Inmediatamente después, llama a opciones(), que ejecuta un bucle while True para mostrar el menú repetidamente. Usando una sentencia match, captura la elección (ya validada) del usuario y delega la tarea a la función correspondiente de los módulos importados, pasándoles siempre la lista de la función paises_en_lista() para que la procesen.


------------------------------------------------------------------
------------------------------------------------------------------


## Instrucciones de uso
Esta guía le orientará sobre cómo interactuar con el programa. Al ejecutar el archivo principal.py, se desplegará el menú principal, que es el centro de control para todas las funcionalidades del sistema.


### 1. Navegación principal
La navegación está diseñada para ser intuitiva. Simplemente ingrese el número de la opción deseada (1-5) y presione "Enter".

El programa está protegido contra entradas erróneas; si usted ingresa una opción no válida (como texto o un número fuera del rango 1-5), el sistema le notificará amablemente y le solicitará que ingrese la opción nuevamente, asegurando que la aplicación no se detenga. Tras completar la mayoría de las acciones, regresará automáticamente a este menú principal.

### 2. Detalle de las opciones del menú
(1) Buscar país por nombre: Esta es una búsqueda directa. El programa le solicitará que ingrese el nombre de un país y el sistema le devolverá toda la información registrada de ese país, o un aviso si no lo encuentra.

(2) Filtrar países: Esta opción le permite explorar los datos. Al seleccionarla, se desplegará un submenú de filtrado (con opciones a, b, c). Aquí podrá elegir si desea ver solo los países de un continente específico, o aquellos dentro de un rango de población o superficie que usted defina.

(3) Ordenar países: Aquí podrá visualizar la base de datos completa de una forma organizada. Al elegir esta opción, accederá al submenú de ordenamiento. Este le permitirá decidir si desea ver la lista ordenada alfabéticamente (por nombre) o numéricamente (de menor a mayor, por población o superficie).

(4) Estadísticas: Esta opción le ofrece un análisis de los datos. Lo llevará al submenú de estadísticas, donde podrá consultar cálculos útiles, como el país con la mayor/menor población o los promedios generales de población y superficie de todos los registros.

(5) Salir: Esta opción finaliza la ejecución del programa y cierra la aplicación de forma segura.


------------------------------------------------------------------
------------------------------------------------------------------

## Ejemplos de entradas y salidas

### Ejemplo 1: Búsqueda de un país específico
En este caso el usuario inicia el programa y busca la información de "japon".

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
(2) Filtrar países
(3) Ordenar países
(4) Estadísticas
(5) Salir

> 1
ingresa el nombre del pais que buscas
> japon

{'nombre': 'japon', 'poblacion': 123201945, 'superficie': 377915, 'continente': 'asia'}

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
...etc


### Ejemplo 2: Filtrado de países por continente
En este caso el usuario decide filtrar la lista para ver unicamente los países registrados en el continente "oceania".

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
(2) Filtrar países
(3) Ordenar países
(4) Estadísticas
(5) Salir

> 2

(a) Filtro por continente
(b) Filtro por poblacion
(c) Filtro por superficie
> a
ingresa un continente
> oceania

<-----paises en oceania----->
+ australia
+ nueva zelanda
<--------------------------------->

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
...etc

### Ejemplo 3: Consulta de Estadísticas (Promedio)
En este caso el usuario desea conocer el promedio de población de todos los países de la lista.

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
(2) Filtrar países
(3) Ordenar países
(4) Estadísticas
(5) Salir

> 4

--- MENÚ ESTADÍSTICAS ---
(1) VER PAÍS CON MENOR POBLACIÓN
(2) VER PAÍS CON MAYOR POBLACIÓN
(3) VER PROMEDIO DE POBLACIÓN DE LOS PAÍSES
(4) VER PROMEDIO DE SUPERFICIE DE LOS PAÍSES

> 3
El promedio de poblacion de todos los países es de 135624092.57142857

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
...etc

### Ejemplo 4: Salida del Programa
Finalmente el usuario decide terminar la sesión.

--- MENÚ PRINCIPAL ---
(1) Buscar país por nombre
(2) Filtrar países
(3) Ordenar países
(4) Estadísticas
(5) Salir

> 5
¡Hasta Luego!

------------------------------------------------------------------
------------------------------------------------------------------

## Integrantes:

--- COMISIÓN 3 | PROGRAMACIÓN 1 ---
        Santiago Ontivero 
        Joaquín Chiarello 
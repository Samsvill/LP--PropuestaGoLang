# LP--PropuestaGoLang



**LENGUAJE DE PROGRAMACIÓN**


**ESPECIFICACIONES PARA ANALIZADOR BÁSICO DE GO EN PLY**

**Grupo 2**

**Integrantes:**

- **Pauta Bueno Alexander Xavier**
- **Pluas Macias Yanaleen Britney**
- **Sanchez Villacreses Samantha Sharid**


**Primer Parcial**

**PAO II 2022**

**Fecha: 06/11/2022**


# Contenido
[Introducción	2](#_Toc119240282)

[Características del lenguaje	2](#_Toc119240283)

[Componentes Léxicos	2](#_Toc119240284)

[Variables.	2](#_Toc119240285)

[Palabras Reservadas.	3](#_Toc119240286)

[Símbolos.	3](#_Toc119240287)

[Operadores aritméticos.	3](#_Toc119240288)

[Operadores Relacionales	4](#_Toc119240289)

[Operadores lógicos.	5](#_Toc119240290)

[Caracteres Especiales.	5](#_Toc119240291)

[Reglas Sintácticas	6](#_Toc119240292)

[Asignación de variables	6](#_Toc119240293)

[Estructuras de Control	6](#_Toc119240294)

[Estructura Condicional Switch	6](#_Toc119240295)

[Estructura Condicional For	7](#_Toc119240296)

[Estructuras de datos (definiciones)	8](#_Toc119240297)

[Strings	9](#_Toc119240298)

[Maps (Sam)	10](#_Toc119240299)

[Expresiones aritméticas	10](#_Toc119240300)

[Expresiones para establecer condiciones:	10](#_Toc119240301)

[Expresiones con conectores lógicos:	10](#_Toc119240302)

[Imprimir e Ingresar datos por teclado. -Xavier	11](#_Toc119240303)

[Reglas Semánticas	12](#_Toc119240304)

[Bibliografía	14](#_Toc119240305)
#




**Introducción**

El lenguaje de programación Go (o también conocido como GoLang) es un lenguaje imperativo multiparadigmático soportado por Google que se lanzó al mercado en el 2009. Es un lenguaje rápido, compilado, y eficiente que consta con su propio garbage collector. Es de rápido aprendizaje y permite gran escalabilidad ya que sus programas se implementan a base de paquetes. No es uno de los lenguajes más reconocidos; sin embargo, se le atribuye una sensación de familiaridad (ya que se puede comparar fácilmente con Python, Java y C).

Es un lenguaje relativamente nuevo, puesto que no tiene el desarrollo que ha tenido los otros grandes competidores. Aun así, sobresale al crear servidores escalables, manejar sistemas de software, incluso escribir programas concurrentes. De acuerdo con Stack Overflow Developer Survey del 2020, Golang subió del noveno al quinto lugar de los LP más queridos. Definitivamente su popularidad y uso crecerá en el futuro, por lo que valdría la pena aprender a usarlo.

Para poder construir el lenguaje basado en GoLang se procederá a usar librerías en Python que se detallan a continuación. La librería PLY (Python Lex & Yacc) es una herramienta totalmente construida en Python. Facilita la implementación de ambas estructuras, lex y yacc, para diseñar un analizador léxico-sintáctico. El módulo lex.py *tokeniza* el texto introducido, siguiendo las reglas que se detallen con las expresiones regulares. Luego, el módulo yacc.py reconocerá la sintaxis del lenguaje con ayuda de una gramática libre de contexto (en esta propuesta se lo analizará con ayuda de la notación metasintáctica BNF (Backus-Naur form)).



**Componentes Léxicos**

***Variables.***

Para declarar variables, se deben tomar en cuenta las siguientes reglas:

- El primer carácter de un identificador debe de ser una letra o un guion bajo (\_).
- El nombre del identificador no puede empezar con un digito
- El nombre del identificador distingue entre mayúsculas y minúsculas
- Puede ser una secuencia de letras y dígitos
- No se puede utilizar las palabras reservadas como if, for, etc como identificadores.

|Identificadores validos:|Identificadores inválidos:|
| :-: | :-: |
|<p>- \_geeks23</p><p>- geeks</p><p>- gek23sd</p><p>- Geeks</p><p>- geeKs</p><p>- geeks\_geeks</p>|<p>- 212geeks</p><p>- If</p><p>- default</p><p></p>|

Además, dentro del lenguaje Go, hay identificadores predeclarados disponibles para constantes, tipos y funciones. No obstante, estos nombres no están reservado y pueden ser utilizados durante la declaración.

- Para constantes: verdadero, falso, un ápice, nada
- Para tipos: int, int8, int16, int32, int64, uint, uint8, uint16, uint32, uint64, uintptr, float32, float64, complex128, complex64, bool, byte, runa, string, error
- Para funciones: hacer, len, gorra, nuevo, anexar, copiar, cerrar, borrar, complejo, real, imag, panic, recuperar

***Palabras Reservadas.***

|break|default|func|interface|select|
| - | - | - | - | - |
|case|defer|go|map|struct|
|chan|else|goto|package|switch|
|const|fallthrough|if|range|type|
|continue|for|import|return|var|
***Símbolos.***

\+    &     +=    &=     &&    ==    !=    (    )

\-    |     -=    |=     ||    <     <=    [    ]

\*    ^     \*=    ^=     <-    >     >=    {    }

/    <<    /=    <<=    ++    =     :=    ,    ;

%    >>    %=    >>=    --    !     ...   .    :

&^          &^=          ~

***Operadores aritméticos.***

Sean “x” y “y”, 10 y 5 respectivamente:


|**Operador**|**Descripción**|**Ejemplo**|
| - | - | - |
|+|Suma los operandos de los extremos.|X + Y resulta 15|
|–|Substrae el operando de la derecha al operando de la izquierda.|X – Y resulta 5|
|\*|Multiplica los operandos de los extremos.|X \* Y resulta 50|
|/|División del número de la izquierda (numerador) entre el número de derecha (denominador).|X / Y resulta 2|
|%|Operador modular o de residuo de división entera.|X / Y resulta 0|
|++|Operador de incremento. Incrementa en 1 el operador de la izquierda. No permite el decremento prefijo (pre-decremento).|X++ resulta 11|
|—|Operador de decremento. Decrementa en 1 el operador de la izquierda, es decir, no permite el decremento prefijo.|X– resulta 9|



**

***Operadores Relacionales***


|**Operador**|**Descripción**|**Ejemplo**|
| - | - | - |
|==|Devuelve verdadero cuando ambos operandos son iguales. Devuelve falso en cualquier otro caso (idéntico a…).|X == Y devuelve falso|
|!=|Devuelve verdadero solamente cuando los operandos son distintos (diferente a…).|X != Y devuelve verdadero|
|>|Devuelve verdadero cuando el operando de la izquierda es mayor que el de la derecha (mayor que…).|X > Y devuelve falso|
|<|Devuelve verdadero cuando el operando de la izquierda es menor que el de la derecha (menor que…).|X < Y devuelve falso|
|>=|Devuelve verdadero cuando el operador de la izquierda es mayor o igual al de la derecha (mayor o igual que..).|X >= Y devuelve falso|
|<=|Devuelve verdadero cuando el operador de izquierda es menor o igual a el de la derecha (menor o igual a…).|Z <= Y devuelve verdadero|


|**A**|**B**|**A & B (conjunción)**|**A | B (disyunción)**|**A ^ B (*XOR*)**|
| :-: | :-: | :-: | :-: | :-: |
|0|0|0|0|0|
|0|1|0|1|1|
|1|0|0|1|1|
|1|1|1|1|0|
***Operadores lógicos.***

***Caracteres Especiales.***

|Carácter de escape|Formato que proporciona|
| :-: | :-: |
|\\|Barra diagonal inversa|
|\"|Comillas dobles|
|\n|Salto de línea|
|\t|Tabulación (sangría)|

**Reglas Sintácticas** 

***Asignación de variables*** 

Para almacenar un valor en una variable utilizamos la palabra reservada var seguido del nombre de la variable, el tipo de dato, un signo igual y el valor que queremos almacenar. Ejemplo:


Otra forma de crear una variable es obviando el tipo de dato en la sentencia ya que el compilador es capaz de inferir el tipo de dato a partir de lo que se almacena en la variable. Ejemplo:



La última forma que se revisará para crear una variable es conocida como declaración corta. Para esto utilizamos el operador **:=** como se muestra a continuación:




**Estructuras de Control**

***Estructura Condicional If*** 

Esta estructura nos permite evaluar una **condición** y en caso de cumplirse** ejecutar un bloque de código que se encuentra entre las llaves.







*Condición* es una expresión que devuelve un valor *bool* (true o false).


***Estructura Condicional Switch*** 

La estructura Switch empieza por la palabra reservada *switch*, seguido de la expresión a evaluar. Luego, lo continúa una serie de casos, llamados *cases*. Cuando nuestra expresión sea igual a alguno de los casos definidos, se ejecutará el código que indique su respectivo *case*. 

Similar a la estructura *if*, se valida que ambas expresiones sean iguales para que se pueda entrar a ese bloque de código. Esta estructura también permite un caso por defecto, denominado *default.* Este último bloque se ejecutará solo si no se encontró ningún caso que sea igual a la expresión. A continuación, un ejemplo breve de la estructura (Doxsey,2021).

switch i {

`	`case 0: fmt.Println("Zero")

`	`case 1: fmt.Println("One")

`	`case 2: fmt.Println("Two")

`	`case 3: fmt.Println("Three")

`	`case 4: fmt.Println("Four")

`	`case 5: fmt.Println("Five")

`	`default: fmt.Println("Unknown Number")

}



***Estructura Condicional For*** 

|Tipo de For|Descripción |Ejemplo|
| - | - | - |
|Ciclo for común|` `Permite ejecutar una o varias líneas de código de manera iterativa pero teniendo el control del valor inicial y final. Es muy parecido a un for utilizado en Java, con la única diferencia que no se necesitan los paréntesis.|<p>package main</p><p>import "fmt"</p><p>func main() {<br>`    `for i := 0; i < 10; i++ {<br>`        `fmt.Println(i)<br>`    `}<br>}</p><p></p>|
|For estilo While|For También puede comportarse como un while en Go. En este caso una instrucción "for" especifica la ejecución repetida de un bloque siempre que una condición booleana se evalúe como verdadera. La condición se evalúa antes de cada iteración. Si la condición está ausente, es equivalente al valor booleano true.|<p>package main</p><p>import "fmt"</p><p>func main() {<br>`    `var i = 0    </p><p>`    `for i < 10 {<br>`        `fmt.Println(i)<br>`        `i++<br>`    `}<br>}</p><p></p>|
|For - range|En esta variación el condicional For nos permitirá recorrer de una manera más fácil las colecciones como arreglos, mapas, entre otros. |<p>package main</p><p>import "fmt"</p><p>func main() {</p><p>`    `for indice, letra := range "hola mundo" {</p><p>`        `fmt.Println(indice, string(letra))</p><p>`    `}</p><p>}</p>|
|For forever|Permite crear un lazo infinito.|<p>package mainimport "fmt"func main() {<br>`    `for {<br>`        `fmt.Println("Hola")<br>`    `}<br>}</p><p></p>|



**Estructuras de datos (definiciones)**

***Array*** 

Una Array es una secuencia numerada de elementos de un solo tipo, denominado tipo de elemento. El número de elementos se denomina longitud del arreglo y nunca es negativo.

La longitud es parte del tipo de la matriz; debe evaluarse como una [constante no negativa ](https://go.dev/ref/spec#Constants)[representable](https://go.dev/ref/spec#Representability) por un valor de tipo int. La longitud de la matriz ase puede descubrir usando la función incorporada [len](#Length_and_capacity). Los elementos se pueden direccionar mediante [índices](https://go.dev/ref/spec#Index_expressions) enteros del 0 al len(a)-1. Los tipos de matrices son siempre unidimensionales, pero pueden estar compuestos para formar tipos multidimensionales.

Para declarar un Array de manera general seria de la siguiente forma

` `var <arrayname>[<length>] <type>

Ejemplo:

var nombres [5]string

Si se quieren ingresar los valores del Array se puede realizar de la siguiente manera 

nombres[0] = "Ana"

nombres[1] = "José"

nombres[2] = "Daniel"

nombres[3] = "María"

nombres [4] = "Carlos"

O de la forma corta:

nombres:= [5]string{"Ana", "José", "Daniel", "María", "Carlos"}


***Strings*** 

Los strings son una secuencia de caracteres que se definen entre comillas dobles. Los strings son inmutables, esto significa que una vez que han sido creados no pueden ser modificados. 

Para definir un string usamos la sintaxis que se vio en asignación de variables.



Los strings se pueden unir mediante el operador **+**. A esta operación se la conoce como concatenación.

***Maps***

Los mapas en Go son colecciones de elementos que se pueden referenciar con un tipo de clave, o *key*. Se detalla su definición acorde a la documentación de Go:

MapType     = "map" "[" [KeyType](https://go.dev/ref/spec#KeyType) "]" [ElementType](https://go.dev/ref/spec#ElementType) .

KeyType     = [Type](https://go.dev/ref/spec#Type) .



Su sintaxis para definirlas es el siguiente:

map[keyType]valueType

Un ejemplo sencillo de como inicializarlas sería el que se detalla a continuación.

nameAgeMap = map[string]int{

`		`"James": 50,

`		`"Ali":   39,

`	`}

**Tipos de expresiones**

***Expresiones aritméticas*** 

Estas expresiones están constituidas mediante el uso de operadores aritméticos y variables o valores introducidos directamente. De forma general se construyen de esta forma: *operando* **operador** *operando*. Ejemplo:






***Expresiones para establecer condiciones***

Estas expresiones están constituidas mediante el uso de operadores de comparación y variables o valores introducidos directamente. De forma general se construyen de esta forma: *operando* **operador** *operando*. Ejemplo:






***Expresiones con conectores lógicos*** 

- **Conjunción (**&&**):** compara dos condiciones (expresiones que devuelven un valor *bool*), devuelve ***true*** si ambas son verdaderas, en cualquier otro caso devuelve ***false***.







- **Disyunción (**||**):** compara dos condiciones (expresiones que devuelven un valor *bool*), devuelve ***false*** si ambas condiciones son falsas, en cualquier otro caso devuelve ***true***.	







- **Negación (**!**):** invierte el valor *bool* de la condición.










**Imprimir e Ingresar datos por teclado. -Xavier**

**Función Básica** 

Para crear una función se debe seguir la siguiente sintaxis:

1. Palabra reservada ***func***
1. Nombre de la función: este debe ser único dentro del ambiente del código 
1. Lista de parámetros: cada parámetro debe estar acompañado de su tipo de dato y separado de los demás mediante una coma. La lista de parámetros es opcional.
1. Lista de tipos de datos a retornar: aquí se debe especificar los tipos de datos de cada valor a retornar separados mediante una coma. Esta lista también es opcional.
1. Cuerpo de instrucciones: bloque de sentencias que se ejecutan al llamar a la función.
1. Palabra reservada ***return***: esta palabra finaliza la función. 
1. Lista de valores de retorno: debe contener los valores a retornar en el **mismo orden** en el que se especificó en la lista de tipos de datos a retornar. Esta lista es opcional.

Ejemplos de funciones:

- Función completa







- Función sin valores de retorno







- Función sin parámetros









**Reglas Semánticas** 

***Conversión entre tipos de datos enteros***

Go tiene muchos tipos de datos enteros entre los que se puede elegir. La elección de uno u otro normalmente se relaciona más con el [rendimiento](https://www.digitalocean.com/community/tutorials/understanding-data-types-in-go#picking-numeric-data-types); sin embargo, habrá veces en las que necesitará realizar conversiones de un tipo de entero a otro. Por ejemplo, Go a veces genera automáticamente valores numéricos como int, que posiblemente no sea su valor de entrada. Si su valor de entrada fuese int64, no podría usar int y los números int64 en la misma expresión matemática sin antes convertir sus tipos de datos para que coincidan.

Suponga que tiene un inst8 y debe convertirlo en un int32. Puede hacer esto ajustándolo en la conversión de tipo int32():

var index int8 = 15

var bigIndex int32

bigIndex = int32(index)

fmt.Println(bigIndex)

Output

15

El operador + no puede usarse entre dos tipos de datos diferentes. Como ejemplo, no puede concatenar cadenas y enteros. Si intenta escribir lo siguiente:

- fmt.Println("Sammy" + 27)

En este caso se obtendría un error de tipo:

Output

cannot convert "Sammy" (type untyped string) to type int

invalid operation: "Sammy" + 27 (mismatched types string and int)


# **Bibliografía**
*CODING OR NOT*. (25 de 06 de 2016). Obtenido de https://codingornot.com/05-go-to-go-operadores

DIGITAL OCEAN. (27 de 02 de 2020). Obtenido de https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-go-es

GO. (s.f.). Obtenido de https://go.dev/ref/spec#Predeclared_identifiers



*Programación estructurada en golang*. (2021) (1.a ed.). Luis Eduardo Muñoz Guerrero. Recuperado de <https://memoriascimted.com/wp-content/uploads/2021/08/Programacion-estructurada-en-Go-lang.pdf> 



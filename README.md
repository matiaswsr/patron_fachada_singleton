Ejemplo para practicar:

Patrones de Diseño: Fachada y Singleton.

Ejemplo de implementación de ambos patrones en Python.

Fachada: patrón para tener un único punto de acceso al sistema y sub sistemas, se encarga de delegar las responsabilidades, dicho de otra forma hace de "pasa manos" con el gestor del servicio definido.

Singleton: nos asegura tener una única instancia de la clase que lo implemente, básicamente se requieren tres cosas para su implementación:

1) Constructor privado de la clase (en caso de Python, se utiliza otra técnica dado que no tenemos como definir un constructor privado).
2) Un atributo estático del mismo tipo que la clase y que guarde su instancia creada.
3) Un método estático y público que verifique y retorne la única instancia que se crea de la clase que implementa el patrón Singleton.

(para la implementación del método del pto. 3 existen variantes)

Autor: M. S.

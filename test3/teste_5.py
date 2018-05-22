def decorador(argumentos_decorador):
    print(argumentos_decorador)
    """Parâmetros do decorador."""
    def decorador_real(func):
        """Receber function."""
        print(func.__name__)
        def execute_function(*argumentos_funcao):
            """Executar function."""
            print(argumentos_funcao)
            pass
        return execute_function
    return decorador_real


@decorador('Anderson')
def soma(x, y):
    return x + y


soma(2, 2)

"""Closue."""
# Ola, Ahoy, Hello


def external(idioma):
    """External function."""
    dic = {'pt': 'Ola', 'pi': 'Ahoy', 'en': 'Hello'}

    def internal(name):
        """Internal function."""
        print('{} {}'.format(dic[idioma], name))
    return internal


func = external('pt')
func('Pedro')
func('Luis')

func = external('en')
func('Pedro')
func('Luis')

func = external('pi')
func('Pedro')
func('Luis')

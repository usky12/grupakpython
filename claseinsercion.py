import time

from random import shuffle

from utils.ordenamientos import insercion1

ordenamientos_validos = \
    {
    'i': 'insercion1',
}

MAX_ITEMS = 5000


class Timer:
    start_process = None
    stop_process = None

    def __init__(self):
        super().__init__()

        self.start_process = time.time() if not self.start_process else self.start_process
        print(f'Iniciando proceso en: {self.start_process}')

    def stop_timer(self):
        self.stop_process = time.time()

    def report_performance(self):
        print(f'Tomó: {self.stop_process - self.start_process} tiempo.')


class Ordenador(Timer):
    """
    ordena una lista por varios métodos
    """
    _tipo = 'insercion1'
    _funcion = None
    _map_ordenamientos = {
       'i': insercion1.ordenamiento_insercion,
    }

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._tipo = kwargs.get('tipo', 'i')
        print(f'Inicializando Ordenador con {self._tipo}.')

        try:
            self._funcion = self._map_ordenamientos[self._tipo]
        except KeyError:
            print(f'Tipo de ordenamiento invalido.')

    def __str__(self):
        return f'{self.__class__.__name__}::ordenando por {self._tipo}'

    def ordenar(self):
        """
        inicia el ordenamiento
        """
        if self._funcion:
            lista = [n for n in range(MAX_ITEMS)]
            shuffle(lista)
            print(f'Ordenando...')
            self._funcion(lista)
            self.stop_timer()
        else:
            print(f'Sin algoritmo de ordenamiento.')
        print(f'Listo!...')
        self.report_performance()


if __name__ == '__main__':
    ordenador = Ordenador()
    ordenador.ordenar()


    ordenador = Ordenador(tipo='i')
    ordenador.ordenar()
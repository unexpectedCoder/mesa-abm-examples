from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid

from game_of_life import CACell as Cell


class GameOfLife(Model):
    """Агентно-ориентированная модель игры *Жизнь*.

    Параметры
    ----------
    * `width`, `height` — размеры клеточного поля
    * `initial_fraction_alive` — доля изначально живых клеток
    * `seed` — затравка генератора случайных чисел
    """

    def __init__(self,
                 width=50,
                 height=50,
                 initial_fraction_alive=0.2,
                 seed=None):
        super().__init__(seed=seed)
        # Инициализация пространства
        self.grid = OrthogonalMooreGrid((width, height), capacity=1, torus=True)
        # Инициализация агентов
        for cell in self.grid.all_cells:
            # Случайное начальное состояние
            state = Cell.ALIVE \
                    if self.random.random() < initial_fraction_alive \
                    else Cell.DEAD
            # Создание и регистрация агента типа Cell
            Cell(self, cell, state)
    
    def step(self):
        """Шаг моделирования.

        Агенты определяют своё следующее состояние,
        а затем обновляют текущее состояние.
        """
        self.agents.do("determine_state")
        self.agents.do("assume_state")

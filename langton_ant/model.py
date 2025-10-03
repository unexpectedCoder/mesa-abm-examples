from mesa import Model
from mesa.discrete_space import OrthogonalVonNeumannGrid

from langton_ant import Ant


class LangtonAnt(Model):
    """Модель клеточного автомата *Муравей Лэнгтона*.

    Параметры
    ----------
    * `width`, `height` — размеры поля
    """

    def __init__(self, width=21, height=21):
        super().__init__()
        # Инициализация пространства с добавлением слоя свойств:
        # свойством будет являться "запах" в клетке автомата (0 или 1)
        self.grid = OrthogonalVonNeumannGrid(
            (width, height), capacity=1, torus=True
        )
        self.grid.create_property_layer(
            "smell", default_value=False, dtype=bool
        )
        # Инициализация агента (муравья) в центре поля
        x, y = width // 2, height // 2
        cell = self.grid.all_cells.select(
            lambda c: c.coordinate[0] == x and c.coordinate[1] == y
        ).cells[0]
        Ant(self, cell)
    
    def step(self):
        """Шаг моделирования.

        1. Определить направление дальнейшего движения
           по текущему состоянию клетки:
           вправо (нет запаха) или влево (запах есть).
        2. Обновить состояние клетки (запах).
        3. Переместиться в определённом направлении.
        """
        self.agents.do("determine_direction")
        self.agents.do("change_smell")
        self.agents.do("move")

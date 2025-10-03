from mesa.discrete_space import Cell, FixedAgent


class CACell(FixedAgent):
    """Агент *Клетка*.
    
    Является агентом с фиксированными координатами —
    реализация клетки клеточного автомата.

    Параметры
    ----------
    * `model` — экземпляр модели Mesa
    * `cell` — экземпляр клетки, в которой находится агент
    * `init_state` — начальное состояние агента
    """

    # Возможные состояния
    DEAD = 0
    ALIVE = 1

    def __init__(self, model, cell: Cell, init_state=DEAD):
        super().__init__(model)
        self.cell = cell
        self.state = init_state
        self._next_state = None
        # _next_state нужно для корректного одновременного обновления
        # состояний всех агентов (клеток автомата)
    
    @property
    def x(self):
        """*x*-координата агента.
        """
        return self.cell.coordinate[0]
    
    @property
    def y(self):
        """*y*-координата агента.
        """
        return self.cell.coordinate[1]
    
    @property
    def is_alive(self):
        """Жив ли агент.
        """
        return self.state == self.ALIVE
    
    @property
    def neighbors(self):
        """Массив агентов из соседних клеток (окрестность Мура).
        """
        return self.cell.neighborhood.agents

    def determine_state(self):
        """Определить следующее состояние на основании состояния соседей.
        """
        live_neighbors = sum(n.is_alive for n in self.neighbors)
        self._next_state = self.state
        # Если агент жив, то...
        if self.is_alive:
            if live_neighbors < 2 or live_neighbors > 3:    # умирает
                self._next_state = self.DEAD
            # иначе продолжает жить
            return
        # Если агент мёртв, то...
        if live_neighbors == 3:     # рождается
            self._next_state = self.ALIVE
        # иначе продолжает быть мёртвым
    
    def assume_state(self):
        """Обновить (принять) текущее состояние.
        """
        self.state = self._next_state

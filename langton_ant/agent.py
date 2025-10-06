import numpy as np
from mesa.discrete_space import Cell, CellAgent


class Ant(CellAgent):
    DIRS = {
        0: np.array((1, 0), dtype=int),
        1: np.array((0, 1), dtype=int),
        2: np.array((-1, 0), dtype=int),
        3: np.array((0, -1), dtype=int)
    }

    def __init__(self, model, cell: Cell):
        super().__init__(model)
        self.cell = cell
        self._dir = 0
    
    @property
    def xy(self):
        return self.cell.coordinate
    
    @property
    def neighborhood(self):
        return self.cell.neighborhood
    
    def determine_direction(self):
        smell = self.cell.smell
        # Есть запах → повернуть налево
        if smell:
            self._dir = (self._dir - 1) % 4
            return
        # Запаха нет → повернуть направо
        self._dir = (self._dir + 1) % 4
    
    def change_smell(self):
        self.cell.smell = not self.cell.smell
    
    def move(self):
        grid_size = self.model.grid.width, self.model.grid.height
        x, y = (self.DIRS[self._dir] + self.xy) % grid_size
        self.cell = self.neighborhood.select(
            lambda c: c.coordinate[0] == x and c.coordinate[1] == y
        ).cells[0]
    

class RLAnt(CellAgent):
    DIRS = {
        0: np.array((1, 0), dtype=int),
        1: np.array((0, 1), dtype=int),
        2: np.array((-1, 0), dtype=int),
        3: np.array((0, -1), dtype=int)
    }

    def __init__(self, model, cell: Cell, rl: str):
        super().__init__(model)
        self.cell = cell
        self._dir = 0
        self._rotors = {
            i: 1 if c == "r" else -1
            for i, c in enumerate(rl.casefold())
        }
        self._n_rotors = len(rl)
    
    @property
    def xy(self):
        return self.cell.coordinate
    
    @property
    def neighborhood(self):
        return self.cell.neighborhood
    
    def determine_direction(self):
        rot = self._rotors[self.cell.smell]
        self._dir = (self._dir + rot) % 4
    
    def change_smell(self):
        self.cell.smell = (self.cell.smell + 1) % self._n_rotors

    def move(self):
        grid_size = self.model.grid.width, self.model.grid.height
        xy = (self.DIRS[self._dir] + self.xy) % grid_size
        self.cell = self.neighborhood.select(
            lambda c: np.all(xy == c.coordinate)
        ).cells[0]

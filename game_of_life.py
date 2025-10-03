from mesa.visualization import SolaraViz, SpaceRenderer
from mesa.visualization.components import AgentPortrayalStyle

from game_of_life import GameOfLife


def agent_portrayal(agent):
    """Описание стиля отображения агентов.
    """
    return AgentPortrayalStyle(
        color="white" if agent.state == 0 else "black",
        marker="s",
        size=30
    )
    

def post_process(ax):
    """Пост-обработка графика.
    """
    ax.set(aspect="equal", xticks=[], yticks=[])


# Описание интерфейса пользователя
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed"
    },
    "width": {
        "type": "SliderInt",
        "value": 50,
        "label": "Width",
        "min": 5,
        "max": 60,
        "step": 1
    },
    "height": {
        "type": "SliderInt",
        "value": 50,
        "label": "Height",
        "min": 5,
        "max": 60,
        "step": 1
    },
    "initial_fraction_alive": {
        "type": "SliderFloat",
        "value": 0.2,
        "label": "Cells initially alive",
        "min": 0,
        "max": 1,
        "step": 0.01
    }
}

# Инициализация модели по умолчанию.
# ВАЖНО, чтобы настраиваемые через интерфейс параметры модели
# имели значения по умолчанию в конструкторе этой самой модели
model = GameOfLife()
# Инициализация рендерера (отображателя)
renderer = SpaceRenderer(model, backend="matplotlib")
renderer.draw_agents(agent_portrayal)
renderer.post_process = post_process

# Создание страницы с описанным выше интерфейсом и рендерером
page = SolaraViz(
    model, renderer, model_params=model_params, name="Game of Life"
)

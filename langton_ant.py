from mesa.visualization import SolaraViz, SpaceRenderer
from mesa.visualization.components import (
    AgentPortrayalStyle, PropertyLayerStyle
)

from langton_ant import LangtonAnt


def agent_portrayal(agent):
    return AgentPortrayalStyle(color="red", marker="+", size=30)


def property_layer_style(layer):
    return PropertyLayerStyle(
        colormap="binary", colorbar=False, alpha=.5
    )


def post_process(ax):
    ax.set(aspect="equal", xticks=[], yticks=[])


model_params = {
    "width": {
        "type": "SliderInt",
        "value": 31,
        "label": "Width",
        "min": 11,
        "max": 101,
        "step": 2
    },
    "height": {
        "type": "SliderInt",
        "value": 31,
        "label": "Height",
        "min": 11,
        "max": 101,
        "step": 2
    }
}

model = LangtonAnt()

renderer = SpaceRenderer(model, backend="matplotlib")
renderer.draw_agents(agent_portrayal)
renderer.draw_propertylayer(property_layer_style)
renderer.post_process = post_process

page = SolaraViz(
    model, renderer, model_params=model_params, name="Langton's Ant"
)

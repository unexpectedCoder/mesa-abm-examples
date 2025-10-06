from mesa.visualization import SolaraViz, SpaceRenderer
from mesa.visualization.components import (
    AgentPortrayalStyle, PropertyLayerStyle
)

from langton_ant import RLAntModel


def agent_portrayal(agent):
    return AgentPortrayalStyle(color="red", marker="+", size=30)


def property_layer_style(layer):
    return PropertyLayerStyle(
        colormap="Greens", colorbar=False, vmin=0, vmax=11
    )


def post_process(ax):
    ax.set(aspect="equal", xticks=[], yticks=[])


rl_model_params = {
    "rotors": {
        "type": "InputText",
        "value": "RL",
        "label": "Rotations"
    },
    "width": {
        "type": "SliderInt",
        "value": 91,
        "label": "Width",
        "min": 81,
        "max": 101,
        "step": 2
    },
    "height": {
        "type": "SliderInt",
        "value": 91,
        "label": "Height",
        "min": 81,
        "max": 121,
        "step": 2
    }
}

model = RLAntModel()
renderer = SpaceRenderer(model, backend="matplotlib")
renderer.draw_agents(agent_portrayal)
renderer.draw_propertylayer(property_layer_style)
renderer.post_process = post_process

page = SolaraViz(
    model, renderer, model_params=rl_model_params, name="RL Ant"
)

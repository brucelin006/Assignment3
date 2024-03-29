from typing import Union
from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def get_fuzzy_output(
    wind_speed: Union[int, float],
    snow_precipitation: Union[int, float],
    show_mf: bool = False,
) -> str:
    if wind_speed is None or snow_precipitation is None:
        raise ValueError("Wind speed and snow precipitation cannot be None.")

    # Convert inputs to float if they are int
    wind_speed = float(wind_speed)
    snow_precipitation = float(snow_precipitation)

    if wind_speed <= 0 or snow_precipitation <= 0:
        raise ValueError(
            "Wind speed and snow precipitation cannot be negative or zero."
        )

    if wind_speed >= 49 or snow_precipitation >= 200:
        raise ValueError(
            "Wind speed and snow precipitation are out of the expected range."
        )

    # Create the universe of discourse
    wind = ctrl.Antecedent(np.arange(10, 50, 1), "wind")
    snow = ctrl.Antecedent(np.arange(0, 201, 1), "snow")
    risk = ctrl.Consequent(np.arange(0, 11, 1), "risk")  # 0 means low, 10 means high

    # Generate fuzzy membership functions
    wind["gentle"] = fuzz.trimf(wind.universe, [0, 0, 20])
    wind["moderate"] = fuzz.trimf(wind.universe, [19, 31, 41])
    wind["strong"] = fuzz.trimf(wind.universe, [39, 44, 49])

    snow["light"] = fuzz.trimf(snow.universe, [0, 0, 76.2])  # up to 3 inches
    snow["moderate"] = fuzz.trimf(
        snow.universe, [50.8, 101.6, 152.4]
    )  # Starts at 2 inches, ends at 6 inches
    snow["heavy"] = fuzz.trimf(snow.universe, [101.6, 152.4, 200])  # beyond 6 inches
    snow["very heavy"] = fuzz.trimf(snow.universe, [152.4, 176.2, 200])

    risk["low"] = fuzz.trimf(risk.universe, [0, 0, 4])
    risk["medium"] = fuzz.trimf(risk.universe, [3, 5, 7])
    risk["high"] = fuzz.trimf(risk.universe, [6, 10, 10])

    # Define fuzzy rules
    rules = []

    rules.append(ctrl.Rule(snow["light"] & wind["gentle"], risk["low"]))
    rules.append(ctrl.Rule(snow["moderate"] | wind["moderate"], risk["medium"]))
    rules.append(ctrl.Rule(snow["heavy"] | wind["strong"], risk["high"]))
    rules.append(ctrl.Rule(snow["very heavy"], risk["high"]))

    # Create control system
    risk_ctrl = ctrl.ControlSystem(rules)

    # Create simulation
    driving = ctrl.ControlSystemSimulation(risk_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    driving.input["wind"] = wind_speed
    driving.input["snow"] = snow_precipitation

    # Crunch the numbers
    driving.compute()

    result = driving.output["risk"]
    print(f"risk: {result:.1f}")

    if show_mf:
        wind.view()
        snow.view()
        risk.view()
        risk.view(sim=driving)
        plt.show()

    if result <= 4:
        return "Low"
    elif result <= 7:
        return "Medium"
    elif result <= 10:
        return "High"
    else:
        return "Unknown"

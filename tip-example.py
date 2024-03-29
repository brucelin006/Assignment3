from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create the universe of discourse
service = ctrl.Antecedent(np.arange(0, 11, 1), "service")
food = ctrl.Antecedent(np.arange(0, 11, 1), "food")
tip = ctrl.Consequent(np.arange(0, 21, 1), "tip")

# Generate fuzzy membership functions
service.automf(names=["poor", "good", "excellent"])
food.automf(names=["bad", "decent", "delicious"])
tip["low"] = fuzz.trimf(tip.universe, [0, 0, 10])
tip["medium"] = fuzz.trimf(tip.universe, [0, 10, 20])
tip["high"] = fuzz.trimf(tip.universe, [10, 20, 20])

# Define the rules
rule1 = ctrl.Rule(service["poor"] | food["bad"], tip["low"])
rule2 = ctrl.Rule(service["good"], tip["medium"])
rule3 = ctrl.Rule(service["excellent"] | food["delicious"], tip["high"])

# Create control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create simulation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
tipping.input["service"] = 7
tipping.input["food"] = 6

# Crunch the numbers
tipping.compute()

print(f"Recommended tip: {tipping.output['tip']:.2f}%")

# You can also plot the result
service.view()
food.view()
tip.view()
tip.view(sim=tipping)
plt.show()

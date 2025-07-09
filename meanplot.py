import matplotlib.pyplot as plt
import numpy as np

# This code plots the mean data for casualties per accident for each of the three runs
run1_means = [6.610299547681407, 6.536865058355343, 6.503955176876471, 6.6607515466955505, 6.508314646065995,
              6.524005327515591, 6.4653593621713314, 6.550733228280108, 6.460580056648923, 6.466639524404651]
run2_means = [4.025544993591556, 3.9455688857687834, 4.000747937888259, 4.004021282454255, 3.9831076856929553,
              4.00645820811186, 3.9665481802769995, 3.9806167233813197, 3.9722644771729234, 4.0194106332513195]
run3_means = [6.710257686658844, 6.88060692800227, 6.69875199816083, 6.775154928532787, 6.816808093070632,
              6.634347403605899, 6.794815124468584, 6.786201670052359, 6.732991404053046, 6.851375427779189]

simulations = np.arange(1, 11)

plt.figure(figsize=(10, 6))

# Plotting each run with labels
plt.plot(simulations, run1_means, label="Run 1 (All Crafts)", marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(simulations, run2_means, label="Run 2 (Without DC8)", marker='o', linestyle='-', color='green', linewidth=2)
plt.plot(simulations, run3_means, label="Run 3 (Without 737 MAX)", marker='o', linestyle='-', color='red', linewidth=2)

plt.xlabel("Simulation Number")
plt.ylabel("Mean Casualties per Accident")
plt.title("Monte Carlo Simulation Means Comparison")

plt.legend()

plt.grid(True)
plt.show()
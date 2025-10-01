import numpy as np
import matplotlib.pyplot as plt

hours = np.arange(24)
temperature = 25 + 5*np.sin((hours-12)*np.pi/12)

plt.plot(hours, temperature, marker='o')
plt.xlabel("Hour of day")
plt.ylabel("Temperature (°C)")
plt.title("Urban Heat – Daily Cycle")
plt.grid(True)
plt.savefig("figure.png", dpi=150, bbox_inches="tight")
print("✅ Simulation finished: figure.png generated")

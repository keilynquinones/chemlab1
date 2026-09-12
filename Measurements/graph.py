#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Measurements
measurements = [0.973, 0.973, 1.00, 0.984, 0.978]
measurement_numbers = [1, 2, 3, 4, 5]

# Average and reference density
average = sum(measurements) / len(measurements)
reference_density = 1.00

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Bar graph
bars = ax.bar(
    measurement_numbers,
    measurements,
    width=0.62,
    color="#3B73C5",
    label="Measurements (g/mL)"
)

# Average and reference density lines
ax.axhline(
    average,
    color="green",
    linestyle=":",
    linewidth=2.5,
    label=f"Average: {average:.3f} g/mL"
)

ax.axhline(
    reference_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Reference density: 1.00 g/mL"
)

# Add measurement values above each bar
for bar, value in zip(bars, measurements):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.005,
        f"{value:.3f}" if value != 1.00 else "1.00",
        ha="center",
        va="bottom",
        fontsize=14
    )

# Labels and title
ax.set_title(
    "Density of water at 23°C by a graduated cylinder",
    fontsize=22,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Measurement Number", fontsize=16, labelpad=12)
ax.set_ylabel("Density (g/mL)", fontsize=16, labelpad=12)

# Y-axis settings
ax.set_ylim(0.90, 1.02)
ax.set_yticks([0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 1.02])

# X-axis settings
ax.set_xticks(measurement_numbers)
ax.set_xticklabels(["1", "2", "3", "4", "5"])

# Tick styling
ax.tick_params(axis="both", labelsize=13)

# Legend
ax.legend(
    loc="upper right",
    fontsize=13,
    frameon=True,
    edgecolor="gray"
)

# Clean up the graph
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Measurements
measurements = [0.991, 0.992, 1.00, 0.992, 0.991]
measurement_numbers = [1, 2, 3, 4, 5]

# Average and reference density
average = sum(measurements) / len(measurements)
reference_density = 1.00

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Bar graph
bars = ax.bar(
    measurement_numbers,
    measurements,
    width=0.62,
    color="#3B73C5",
    label="Measurements (g/mL)"
)

# Average and reference density lines
ax.axhline(
    average,
    color="green",
    linestyle=":",
    linewidth=2.5,
    label=f"Average: {average:.3f} g/mL"
)

ax.axhline(
    reference_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Reference density: 1.00 g/mL"
)

# Add measurement values above each bar
for bar, value in zip(bars, measurements):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.005,
        f"{value:.3f}" if value != 1.00 else "1.00",
        ha="center",
        va="bottom",
        fontsize=14
    )

# Labels and title
ax.set_title(
    "Density of water at 23°C by a volumetric pipette",
    fontsize=22,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Measurement Number", fontsize=16, labelpad=12)
ax.set_ylabel("Density (g/mL)", fontsize=16, labelpad=12)

# Y-axis settings
ax.set_ylim(0.90, 1.02)
ax.set_yticks([0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 1.02])

# X-axis settings
ax.set_xticks(measurement_numbers)
ax.set_xticklabels(["1", "2", "3", "4", "5"])

# Tick styling
ax.tick_params(axis="both", labelsize=13)

# Legend
ax.legend(
    loc="upper right",
    fontsize=13,
    frameon=True,
    edgecolor="gray"
)

# Clean up the graph
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

plt.tight_layout()
plt.show()
#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Measurements
measurements = [0.973, 0.973, 1.00, 0.984, 0.978]
measurement_numbers = [1, 2, 3, 4, 5]

# Average and reference density
average = sum(measurements) / len(measurements)
reference_density = 0.997

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
    label="Reference density: 0.997 g/mL"
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
average = 0.993
reference_density = 1.00

# Standard deviation used for the error bars
error = 0.0038

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Bar graph with error bars
bars = ax.bar(
    measurement_numbers,
    measurements,
    width=0.62,
    color="#3B73C5",
    yerr=error,
    capsize=5,
    ecolor="black",
    error_kw={"elinewidth": 1.5},
    label="Measurements (g/mL)"
)

# Average line
ax.axhline(
    average,
    color="green",
    linestyle=":",
    linewidth=2.5,
    label="Average: 0.993 g/mL"
)

# Reference density line
ax.axhline(
    reference_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Reference density: 0.997 g/mL"
)

# Add measurement values above each bar
for bar, value in zip(bars, measurements):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + error + 0.001,
        f"{value:.3f}" if value != 1.00 else "1.00",
        ha="center",
        va="bottom",
        fontsize=14
    )

# Title
ax.set_title(
    "Density of water at 22°C by a volumetric pipette",
    fontsize=22,
    fontweight="bold",
    pad=20
)

# Axis labels
ax.set_xlabel(
    "Measurement Number",
    fontsize=16,
    labelpad=12
)

ax.set_ylabel(
    "Density (g/mL)",
    fontsize=16,
    labelpad=12
)

# Y-axis settings
ax.set_ylim(0.90, 1.02)
ax.set_yticks([
    0.90,
    0.92,
    0.94,
    0.96,
    0.98,
    1.00,
    1.02
])

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

# Clean up graph
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

# Adjust spacing
plt.tight_layout()

# Display graph
plt.show()
import matplotlib.pyplot as plt

# Measurements
measurements = [0.973, 0.973, 1.00, 0.984, 0.978]
measurement_numbers = [1, 2, 3, 4, 5]

# Average and reference density
average = 0.982
reference_density = 0.997

# Standard deviation used for the error bars
error = 0.0038

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Bar graph with error bars
bars = ax.bar(
    measurement_numbers,
    measurements,
    width=0.62,
    color="#3B73C5",
    yerr=error,
    capsize=5,
    ecolor="black",
    error_kw={"elinewidth": 1.5},
    label="Measurements (g/mL)"
)

# Average line
ax.axhline(
    average,
    color="green",
    linestyle=":",
    linewidth=2.5,
    label="Average: 0.993 g/mL"
)

# Reference density line
ax.axhline(
    reference_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Reference density: 0.997 g/mL"
)

# Add measurement values above each bar
for bar, value in zip(bars, measurements):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + error + 0.001,
        f"{value:.3f}" if value != 1.00 else "1.00",
        ha="center",
        va="bottom",
        fontsize=14
    )

# Title
ax.set_title(
    "Density of water at 23°C by a graduated cylinder",
    fontsize=22,
    fontweight="bold",
    pad=20
)

# Axis labels
ax.set_xlabel(
    "Measurement Number",
    fontsize=16,
    labelpad=12
)

ax.set_ylabel(
    "Density (g/mL)",
    fontsize=16,
    labelpad=12
)

# Y-axis settings
ax.set_ylim(0.90, 1.02)
ax.set_yticks([
    0.90,
    0.92,
    0.94,
    0.96,
    0.98,
    1.00,
    1.02
])

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

# Clean up graph
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(False)

# Adjust spacing
plt.tight_layout()

# Display graph
plt.show()
import matplotlib.pyplot as plt

# Measurements
measurements = [7.94, 7.94, 7.94, 7.94]
measurement_numbers = [1, 2, 3, 4]

# Average and reference density
average = sum(measurements) / len(measurements)

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

# Average line
ax.axhline(
    average,
    color="green",
    linestyle=":",
    linewidth=2.5,
    label=f"Average: {average:.3f} g/mL"

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
    "Density of a penny",
    fontsize=22,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Measurement Number", fontsize=16, labelpad=12)
ax.set_ylabel("Density (g/cm³)", fontsize=16, labelpad=12)

# Y-axis settings
ax.set_ylim(7.86, 7.98)
ax.set_yticks([7.86, 7.88, 7.90, 7.92, 7.94, 7.96, 7.98])

# X-axis settings
ax.set_xticks(measurement_numbers)
ax.set_xticklabels(["1", "2", "3", "4"])

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
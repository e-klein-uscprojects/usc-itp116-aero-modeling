import pandas as pd
import matplotlib.pyplot as plt
from models.flight_optimizer import optimize_flight

# Load and optimize flight data
df = pd.read_csv('data/sample_routes.csv')
optimized_df = optimize_flight(df)

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(df['route_id'], df['duration'], label='Original Duration', marker='o')
plt.plot(df['route_id'], optimized_df['optimized'], label='Optimized Duration', marker='x')
plt.title('Flight Route Optimization')
plt.xlabel('Route ID')
plt.ylabel('Duration (minutes)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('results/flight_duration_comparison.png')
plt.show()


import pandas as pd
from models.flight_optimizer import optimize_flight

# Load the sample dataset
df = pd.read_csv('data/sample_routes.csv')

# Run the optimization
optimized_df = optimize_flight(df)

# Show the results
print(optimized_df)


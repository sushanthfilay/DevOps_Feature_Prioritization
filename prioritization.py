import pandas as pd

# Define features with RICE scoring criteria
features = [
    {"Feature": "Automated Rollback", "Reach": 4, "Impact": 5, "Confidence": 4, "Effort": 3},
    {"Feature": "Logging & Monitoring", "Reach": 5, "Impact": 4, "Confidence": 5, "Effort": 4},
    {"Feature": "Blue-Green Deployment", "Reach": 3, "Impact": 5, "Confidence": 3, "Effort": 5},
    {"Feature": "Database Optimization", "Reach": 4, "Impact": 4, "Confidence": 4, "Effort": 4},
    {"Feature": "Security Patch Automation", "Reach": 3, "Impact": 5, "Confidence": 5, "Effort": 3}
]

# Convert to DataFrame
df = pd.DataFrame(features)

# Calculate RICE Score: (Reach * Impact * Confidence) / Effort
df["RICE Score"] = (df["Reach"] * df["Impact"] * df["Confidence"]) / df["Effort"]

# Sort features by RICE score (highest first)
df = df.sort_values(by="RICE Score", ascending=False)

# Save to CSV
df.to_csv("feature_prioritization.csv", index=False)

# Print results
print(df)

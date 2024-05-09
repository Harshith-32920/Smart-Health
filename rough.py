import pickle
import numpy as np

# Utility script for testing trained pickle risk models
def inspect_model(model_path):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            print(f"Successfully loaded {model_path}: {type(model)}")
            return model
    except FileNotFoundError:
        print(f"File {model_path} not found.")
        return None

if __name__ == "__main__":
    print("Testing risk model loading pipeline...")
    inspect_model("diabetes_risk_model.pkl")

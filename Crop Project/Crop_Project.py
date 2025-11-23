import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report
import os



class DataManager:
    def __init__(self, path):
        self.path = path
        self.df = None

    def read_csv(self):

        if not os.path.exists(self.path):
            print("File not found! Check path.")
            return None

        self.df = pd.read_csv(self.path)

        return self.df

    def get_split_data(self):

        X = self.df.iloc[:, :-1]
        y = self.df.iloc[:, -1]
        return X, y



class PreProcessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def split_and_scale(self, X, y):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



        return X_train, X_test, y_train, y_test



class CropPredictor:
    def __init__(self):

        self.model = RandomForestClassifier(n_estimators=20, random_state=42)

    def fit_model(self, x, y):
        self.model.fit(x, y)

    def get_accuracy(self, x_test, y_test):
        preds = self.model.predict(x_test)
        acc = accuracy_score(y_test, preds)
        return acc

    def get_report(self, x_test, y_test):
        preds = self.model.predict(x_test)
        return classification_report(y_test, preds)

    def predict_one(self, data):
        return self.model.predict(data)



class StatsPrinter:
    def print_start(self):
        print("------------------------------------------------")
        print("Starting Crop Recommendation Project...")
        print("------------------------------------------------")


# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":

    printer = StatsPrinter()
    printer.print_start()


    path = 'data/Crop_recommendation.csv'


    loader = DataManager(path)
    df = loader.read_csv()

    if df is not None:
        print("Data Loaded. Shape:", df.shape)

        X, y = loader.get_split_data()


        processor = PreProcessor()
        X_train, X_test, y_train, y_test = processor.split_and_scale(X, y)


        print("Training Model...")
        model = CropPredictor()
        model.fit_model(X_train, y_train)


        acc = model.get_accuracy(X_test, y_test)
        print(f"Accuracy achieved: {acc * 100:.2f}%")

        print("\nGenerating Report...")
        print(model.get_report(X_test, y_test))


        # input = [N, P, K, Temp, Hum, pH, Rain]
        test_input = [[90, 42, 43, 20.87, 82.0, 6.5, 202.93]]
        res = model.predict_one(test_input)
        print("Testing with sample input:", test_input)
        print("Predicted Crop:", res[0])

    else:
        print("Exiting...")
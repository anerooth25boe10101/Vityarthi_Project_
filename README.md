# Vityarthi_Project_
An AI-powered application that recommends optimal crops based on soil nutrients and weather parameters using Random Forest Classification.
# Smart Crop Recommendation System

## 1. Project Overview
The **Smart Crop Recommendation System** is a Machine Learning application developed in the field of bioengineering and agriculture, selecting the right crop for specific soil conditions is critical for maximizing yield. This system solves that problem by analyzing environmental parameters (such as soil nutrients and weather conditions) to predict the most suitable crop for cultivation.

## 2. Features
* **Data Ingestion:** automated loading and validation of agricultural datasets (CSV format).
* **Data Preprocessing:** Splits data into training and testing sets and scales features for optimal performance.
* **ML Classification:** Uses a **Random Forest Classifier** to categorize soil inputs into one of 22 distinct crop types.
* **Performance Metrics:** Automatically calculates and displays model accuracy, precision, recall, and F1-score.
* **Live Prediction:** Includes a simulation module that accepts new soil data inputs and outputs a recommended crop.

## 3. Technologies & Tools Used
* **Language:** Python 3.x
* **Libraries:**
    * `pandas`: For data manipulation and CSV handling.
    * `numpy`: For numerical computations.
    * `scikit-learn`: For implementing the Random Forest algorithm and evaluation metrics.
* **Tools:** VS Code (or PyCharm), Git & GitHub.

## 4. Steps to Install & Run
Follow these steps to set up the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_REPO_LINK_HERE>
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd Crop_Project
    ```
3.  **Install Dependencies:**
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Verify Data:**
    Make sure the `Crop_recommendation.csv` file is located inside the `data/` folder.
5.  **Run the Application:**
    ```bash
    python main.py
    ```

## 5. Instructions for Testing
The system is designed to run an automated testing sequence immediately upon execution:
1.  **Execute the Script:** Run `python main.py`.
2.  **View Training Results:** The console will display the "Accuracy achieved" (expected >99%) and a detailed Classification Report.
3.  **Verify Logic:** The script concludes with a "Testing with sample input" section. Check that the output matches the expected crop for the hardcoded values (e.g., Nitrogen=90 -> Rice).

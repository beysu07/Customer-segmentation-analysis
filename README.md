# Customer Segmentation Analysis

This project analyzes customer behavior using the `Mall_Customers.csv` dataset and applies the K-Means clustering algorithm to create customer segments. The goal is to identify different customer groups to develop targeted marketing strategies.

## Project Goal

The project groups customers based on their annual income and spending score. This segmentation helps marketing teams to target their campaigns more effectively. For instance, special VIP campaigns can be designed for high-income but low-spending customers.

## Technologies Used

*   **Python**
*   **Pandas:** For data manipulation and reading CSV files.
*   **Scikit-learn:** For building the K-Means clustering model.
*   **Matplotlib:** For data visualization (pie chart, histogram, scatter plot).
*   **NumPy:** For numerical operations (used implicitly by other libraries).

## Setup and Usage

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```

2.  **Install necessary libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the analysis**:
    ```bash
    python main.py
    ```
    When the script runs, it will display the analysis steps and generate the plots.

## Dataset

The `Mall_Customers.csv` file used in the project contains the following information about customers of a shopping mall:
*   `CustomerID`: Unique identifier for each customer.
*   `Gender`: Gender of the customer.
*   `Age`: Age of the customer.
*   `Annual Income (k$)`: Annual income of the customer in thousands of dollars.
*   `Spending Score (1-100)`: A score assigned by the mall based on customer behavior and spending habits (1-100, where 100 is high spending).

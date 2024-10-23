# Create Sample Dataset

## About This Project

The **Create Sample Dataset** project is a Python script designed to generate a synthetic dataset for testing and development purposes. It utilizes the Faker library to create realistic sample data, making it ideal for use in applications where you need a dataset without relying on real user data. This can be especially useful for testing, training models, or prototyping applications.


## Features
- Generates a variety of data types including names, addresses, emails, and more.
- Customizable dataset size.
- Outputs data to CSV files for easy access and integration.


## Prerequisites
Before running the code, ensure you have the following installed:
- Python 3.6 or higher
- Pip (Python package installer)


## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/lamorasjr/create-sample-dataset.git
    
    cd create-sample-dataset
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
- On Windows:
    ```bash
    venv\Scripts\activate
    ```

- On macOS/Linux:
    ``` bash
    source venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the script using Python:

```bash
python generate_data.py
```

Upon execution, the script will generate sample datasets and save them as CSV files in the project directory. You can adjust the parameters within the script to customize the dataset to your needs.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.
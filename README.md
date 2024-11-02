# Create Sample Dataset

## About This Project

This project is a Python script designed to generate a fake dataset for testing and development purposes. It utilizes the Faker library to create sample data for a star schema data model for analytics tasks.

## Prerequisites
Before running the code, ensure you have the following installed:
- Python 3.12.1 or higher
- Pyenv
- Poetry


## Install and run the project
1. Clone the repository:

    ```bash
    git clone https://github.com/lamorasjr/create-sample-dataset.git
    
    cd create-sample-dataset
    ```

2. Create the virtual enviroment and install the dependencies with Poetry:
    ```bash
    poetry install
    ```

3. Activate the virtual environment:
    ```bash
    poetry shell
    ```

4. Run the script using Python:

    ```bash
    poetry run python src/generate_dataset.py
    ```

Upon execution, the script will generate sample datasets and save them as CSV files in the project directory. You can adjust the parameters within the script to customize the dataset to your needs.


## Adjusting dataset generator parameters
* Access the file located at: `src/generate_dataset.py`
* Adjust the parameters numbers for variables:
    * num_customers
    * num_products
    * num_sales
    * start_date
    * end_date
    * output_path
* Save the code, then run it

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.
# duck_project

- This project is built using dbt with DuckDB for local analyses and transformation workflows.
- The raw dataset is provided in the ``seeds/`` directory and is used as the starting point for all transformations.

## Getting Started
To run the project,
1. Initial Data Preparation:

Run Fashionable.py to clean and standardize the raw dataset.

2. Build Models:

Run ``dbt run``

3. Run Tests:

Run ``dbt test``

4. Analysis Scripts:

Explore additional insights and graphs by running any of the Python scripts:
Trends.py, Revenue.py


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)

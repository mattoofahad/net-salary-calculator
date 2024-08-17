---
title: Net Salary Calculate
emoji: 💵🤑🫰
colorFrom: green
colorTo: green
sdk: streamlit
sdk_version: 1.37.1
app_file: app.py
pinned: false
---


# Salary Calculator

This Salary Calculator is a Python-based command-line tool designed to help users determine the additional amount needed on top of their desired salary to account for taxes. It takes into consideration factors such as current salary, desired increment, daily travel costs, and the number of physical workdays per week.

## Getting Started

### A. Prerequisites

- Conda environment manager
- Python version 3.11

### B. Setting Up the Environment

1. **Create and activate a Conda environment**:
   - Create: `conda create -n salary_calc_env python=3.11 -y`
   - Activate: `conda activate salary_calc_env`
   - **Note**: You can replace `salary_calc_env` with your preferred environment name.

2. **Install required packages**: 
   ```bash
   pip install -r requirements.txt
   ```

### C. Running the Application

- Using default values:
  ```bash
  python salary_calculator.py 90000
  ```
  This uses default values of `desired_increment_percentage=0.3`, `daily_cost_of_travel=1500`, and `physical_days_per_week=5`.

- Using custom values:
  ```bash
  python salary_calculator.py 220000 --desired-increment-percentage 0.10 --daily-cost-of-travel 2000 --physical-days-per-week 3
  ```
F
- For help and to see all available options:
  ```bash
  python salary_calculator.py --help
  ```

## Features

- Calculates the additional amount needed to achieve the desired net salary after tax deductions
- Considers factors like current salary, desired increment, daily travel costs, and work schedule
- Provides a detailed breakdown of the calculation results
- Offers flexibility to use default values or specify custom inputs

## TODO
- RestAPI server
- Streamlit application
- workflow to deploy in hugging face

## Contributing

Feel free to fork this project and submit pull requests with any enhancements or bug fixes. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.


git push https://mattoofahad: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@huggingface.co/spaces/mattoofahad/net-salary-calculate main

git push --force https://mattoofahad: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@huggingface.co/spaces/mattoofahad/net-salary-calculate main
class Constants:
    DEFAULT_CURRENT_SALARY = 100000.0
    DEFAULT_INCREMENT_PERCENTAGE = 0.3
    DEFAULT_DAILY_TRAVEL_COST = 1500
    DEFAULT_PHYSICAL_DAYS = 5
    DEFAULT_INITIAL_NET = 212500.0
    DEFAULT_CURRENT_SALARY_WITH_TAX = 200000.0
    DEFAULT_YEARLY_SALARY_WITH_TAX = 1500000.0

    DEFAULT_TAX_BRACKETS = [
        (0, 600000, 0),
        (600000, 1200000, 0.05),
        (1200000, 2200000, 0.15),
        (2200000, 3200000, 0.25),
        (3200000, 4100000, 0.30),
        (4100000, float("inf"), 0.35),
    ]

class Styles:
    METRIC_STYLE = """
    <style>
    .metric-container {
        background-color: #f0f2f6;
        border-radius: 7px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .metric-label {
        font-size: 14px;
        color: #555;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #0066cc;
    }
    </style>
    """
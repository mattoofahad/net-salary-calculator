def calculate_monthly_tax(monthly_income):
    annual_income = monthly_income * 12
    tax_brackets = [
        (0, 600000, 0),
        (600000, 1200000, 0.05),
        (1200000, 2200000, 0.15),
        (2200000, 3200000, 0.25),
        (3200000, 4100000, 0.30),
        (4100000, float("inf"), 0.35),
    ]
    total_tax = 0
    remaining_income = annual_income
    for lower, upper, rate in tax_brackets:
        if remaining_income <= 0:
            break

        taxable_amount = min(remaining_income, upper - lower)
        tax = taxable_amount * rate
        total_tax += tax
        remaining_income -= taxable_amount
    monthly_tax = total_tax / 12
    return round(monthly_tax, 2)


def calculate_net_salary(gross_salary):
    return gross_salary - calculate_monthly_tax(gross_salary)


def calculated_initial_desired_net(
    current_salary, desired_increment, daily_cost_of_travel, physical_days_per_week
):
    return (current_salary + current_salary * desired_increment) + (
        daily_cost_of_travel * physical_days_per_week * 4.5
    )


def calculate_additional_amount(initial_desired_net):
    gross_salary = initial_desired_net
    max_iterations = 100
    for _ in range(max_iterations):
        net_salary = calculate_net_salary(gross_salary)
        if abs(net_salary - initial_desired_net) < 0.01:
            break
        gross_salary += initial_desired_net - net_salary
    additional_amount = gross_salary - initial_desired_net

    return {
        "initial_desired_net": round(initial_desired_net, 2),
        "gross_salary_needed": round(gross_salary, 2),
        "additional_amount": round(additional_amount, 2),
        "tax": round(calculate_monthly_tax(gross_salary), 2),
        "final_net_salary": round(calculate_net_salary(gross_salary), 2),
    }

from typing import Optional

import typer
import pandas as pd
from constants import Constants
from functions import Functions

app = typer.Typer()

tax_brackets_df = pd.DataFrame(
    Constants.DEFAULT_TAX_BRACKETS, columns=["Lower Limit", "Upper Limit", "Tax Rate"]
)


@app.command()
def calculate_salary(
    current_salary: int = typer.Argument(..., help="Current monthly salary in PKR"),
    desired_increment_percentage: Optional[float] = typer.Option(
        0.3, help="Desired salary increment as a decimal (e.g., 0.3 for 30%)"
    ),
    daily_cost_of_travel: Optional[int] = typer.Option(
        1500, help="Daily cost of travel in PKR"
    ),
    physical_days_per_week: Optional[int] = typer.Option(
        5, help="Number of physical days per week"
    ),
):
    """
    Calculate the additional amount needed for desired salary after tax adjustment.
    """
    initial_desired_net = Functions.calculated_initial_desired_net(
        current_salary,
        desired_increment_percentage,
        daily_cost_of_travel,
        physical_days_per_week,
    )
    result = Functions.calculate_additional_amount(initial_desired_net, tax_brackets_df)

    typer.echo("Salary Calculation Results")
    typer.echo("--------------------------")
    typer.echo(
        f"{'Initial Desired Net Salary':<30} PKR {result['initial_desired_net']:>13,.2f}"
    )
    typer.echo(
        f"{'Gross Salary Needed':<30} PKR {result['gross_salary_needed']:>13,.2f}"
    )
    typer.echo(
        f"{'Additional Amount Needed':<30} PKR {result['additional_amount']:>13,.2f}"
    )
    typer.echo(f"{'Tax':<30} PKR {result['tax']:>13,.2f}")
    typer.echo(f"{'Final Net Salary':<30} PKR {result['final_net_salary']:>13,.2f}")


if __name__ == "__main__":
    app()

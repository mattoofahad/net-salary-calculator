import typer
from typing import Optional

from functions import calculated_initial_desired_net, calculate_additional_amount

app = typer.Typer()


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
    initial_desired_net = calculated_initial_desired_net(
        current_salary, desired_increment_percentage, daily_cost_of_travel, physical_days_per_week
    )
    result = calculate_additional_amount(initial_desired_net)

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

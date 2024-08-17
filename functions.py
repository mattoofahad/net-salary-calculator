from constants import Styles, Constants
import streamlit as st


class Functions:
    @staticmethod
    def calculated_current_salary_after_tax(current_salary, tax_brackets):
        return current_salary - Functions.calculate_monthly_tax(
            current_salary, tax_brackets
        )

    @staticmethod
    def calculate_monthly_tax(monthly_income, tax_brackets):
        annual_income = monthly_income * 12
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

    @staticmethod
    def calculate_net_salary(gross_salary, tax_brackets):
        return gross_salary - Functions.calculate_monthly_tax(
            gross_salary, tax_brackets
        )

    @staticmethod
    def calculated_initial_desired_net(
        current_salary, desired_increment, daily_cost_of_travel, physical_days_per_week
    ):
        return (current_salary + current_salary * desired_increment) + (
            daily_cost_of_travel * physical_days_per_week * 4.5
        )

    @staticmethod
    def calculate_additional_amount(initial_desired_net, tax_brackets):
        gross_salary = initial_desired_net
        max_iterations = 100
        for _ in range(max_iterations):
            net_salary = Functions.calculate_net_salary(gross_salary, tax_brackets)
            if abs(net_salary - initial_desired_net) < 0.01:
                break
            gross_salary += initial_desired_net - net_salary
        additional_amount = gross_salary - initial_desired_net

        return {
            "initial_desired_net": round(initial_desired_net, 2),
            "gross_salary_needed": round(gross_salary, 2),
            "additional_amount": round(additional_amount, 2),
            "tax": round(
                Functions.calculate_monthly_tax(gross_salary, tax_brackets), 2
            ),
            "final_net_salary": round(
                Functions.calculate_net_salary(gross_salary, tax_brackets), 2
            ),
        }


import pandas as pd


class StreamlitFunctions:
    @staticmethod
    def update_initial_salary_parameter():
        # if (
        #     st.session_state.user_initial_desired_net_state
        #     < st.session_state.current_salary
        # ):
        #     st.session_state.user_initial_desired_net = (
        #         st.session_state.current_salary
        #         + st.session_state.user_initial_desired_net_state
        #     )
        # else:
        st.session_state.user_initial_desired_net = (
            st.session_state.user_initial_desired_net_state
        )

    @staticmethod
    def reset_initial_salary_parameter():
        def reset_values():
            st.session_state.user_initial_desired_net = Constants.DEFAULT_INITIAL_NET
            st.session_state.valid_input = True

        st.button(
            "Reset Final Desired Net Salary Value",
            on_click=reset_values,
            use_container_width=True,
        )

    @staticmethod
    def initial_salary_parameter():
        st.header("Final Desired Net Salary")
        if st.session_state.user_initial_desired_net >= st.session_state.current_salary:
            minimum_value = st.session_state.current_salary
        else:
            minimum_value = 0.0
        st.number_input(
            "Final Desired Net Salary (PKR)",
            min_value=minimum_value,
            value=st.session_state.user_initial_desired_net,
            step=1000.0,
            key="user_initial_desired_net_state",
            on_change=StreamlitFunctions.update_initial_salary_parameter,
        )

    @staticmethod
    def reset_tax_brackets():
        def reset_values():
            st.session_state.tax_brackets = Constants.DEFAULT_TAX_BRACKETS

        st.button(
            "Reset Tax Brackets",
            use_container_width=True,
            on_click=reset_values,
        )

    @staticmethod
    def reset_salary_parameters():
        def reset_values():
            st.session_state.current_salary = Constants.DEFAULT_CURRENT_SALARY
            st.session_state.desired_increment_percentage = (
                Constants.DEFAULT_INCREMENT_PERCENTAGE
            )
            st.session_state.daily_cost_of_travel = Constants.DEFAULT_DAILY_TRAVEL_COST
            st.session_state.physical_days_per_week = Constants.DEFAULT_PHYSICAL_DAYS

        st.button(
            "Reset Salary Parameters Values",
            use_container_width=True,
            on_click=reset_values,
        )

    @staticmethod
    def reset_tax_on_current_salary():
        def reset_values():
            st.session_state.tax_on_current_salary = (
                Constants.DEFAULT_CURRENT_SALARY_WITH_TAX
            )

        st.button(
            "Reset Current Salary",
            use_container_width=True,
            on_click=reset_values,
        )

    @staticmethod
    def print_tax_on_current_salary():
        st.header("Tax on Current Salary")

        def update_tax_on_current_salary_parameter():
            st.session_state.tax_on_current_salary = (
                st.session_state.tax_on_current_salary_state
            )

        st.number_input(
            "Current monthly Salary (PKR)",
            min_value=0.0,
            step=1000.0,
            value=st.session_state.tax_on_current_salary,
            key="tax_on_current_salary_state",
            on_change=update_tax_on_current_salary_parameter,
        )

    @staticmethod
    def print_salary_parameters():
        st.header("Salary Parameters")

        def update_current_salary_parameter():
            st.session_state.current_salary = st.session_state.current_salary_state

        st.number_input(
            "Current monthly salary after Tax (PKR)",
            min_value=0.0,
            step=1000.0,
            value=st.session_state.current_salary,
            key="current_salary_state",
            on_change=update_current_salary_parameter,
        )

        def update_desired_increment_percentage_parameter():
            st.session_state.desired_increment_percentage = (
                st.session_state.desired_increment_percentage_state
            )

        st.number_input(
            "Desired salary increment (as a decimal)",
            min_value=0.0,
            step=0.05,
            value=st.session_state.desired_increment_percentage,
            format="%.2f",
            key="desired_increment_percentage_state",
            on_change=update_desired_increment_percentage_parameter,
        )

        def update_daily_cost_of_travel_parameter():
            st.session_state.daily_cost_of_travel = (
                st.session_state.daily_cost_of_travel_state
            )

        st.number_input(
            "Daily cost of travel (PKR)",
            min_value=0,
            step=100,
            value=st.session_state.daily_cost_of_travel,
            key="daily_cost_of_travel_state",
            on_change=update_daily_cost_of_travel_parameter,
        )

        def update_physical_days_per_week_parameter():
            st.session_state.physical_days_per_week = (
                st.session_state.physical_days_per_week_state
            )

        st.number_input(
            "Number of On-Site days per week",
            min_value=0,
            max_value=7,
            step=1,
            value=st.session_state.physical_days_per_week,
            key="physical_days_per_week_state",
            on_change=update_physical_days_per_week_parameter,
        )

    @staticmethod
    def print_tax_brackets():
        st.header("Tax Brackets")
        tax_brackets_df = pd.DataFrame(
            st.session_state.tax_brackets,
            columns=["Lower Limit", "Upper Limit", "Tax Rate"],
        )

        edited_tax_brackets = st.data_editor(
            tax_brackets_df, num_rows="dynamic", use_container_width=True
        )
        st.session_state.tax_brackets = list(
            edited_tax_brackets.itertuples(index=False, name=None)
        )

    @staticmethod
    def initialize_session_values():
        st.title("Net Salary Calculator")
        if "tax_brackets" not in st.session_state:
            st.session_state.tax_brackets = Constants.DEFAULT_TAX_BRACKETS
        if "tax_on_current_salary" not in st.session_state:
            st.session_state.tax_on_current_salary = (
                Constants.DEFAULT_CURRENT_SALARY_WITH_TAX
            )
        if "current_salary" not in st.session_state:
            st.session_state.current_salary = Constants.DEFAULT_CURRENT_SALARY
        if "desired_increment_percentage" not in st.session_state:
            st.session_state.desired_increment_percentage = (
                Constants.DEFAULT_INCREMENT_PERCENTAGE
            )
        if "daily_cost_of_travel" not in st.session_state:
            st.session_state.daily_cost_of_travel = Constants.DEFAULT_DAILY_TRAVEL_COST
        if "physical_days_per_week" not in st.session_state:
            st.session_state.physical_days_per_week = Constants.DEFAULT_PHYSICAL_DAYS
        if "user_initial_desired_net" not in st.session_state:
            st.session_state.user_initial_desired_net = Constants.DEFAULT_INITIAL_NET
            
        if "type_to_calculate" not in st.session_state:
            st.session_state.type_to_calculate = None
        
    @staticmethod
    def custom_metric(label, value):
        st.markdown(Styles.METRIC_STYLE, unsafe_allow_html=True)
        st.markdown(
            f"""
        <div class="metric-container">
            <div class="metric-label">{label}</div>
            <div class="metric-value">PKR {value:,.2f}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

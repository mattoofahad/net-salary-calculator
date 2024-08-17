import streamlit as st

from functions import Functions, StreamlitFunctions
import pandas as pd


def calculate_salary_parameters():
    st.session_state.type_to_calculate = "salary_parameters"


def calculate_initial_salary_parameter():
    st.session_state.type_to_calculate = "desired_salary"


def calculate_tax_on_current_salary():
    st.session_state.type_to_calculate = "tax_on_current_salary"


StreamlitFunctions.initialize_session_values()
StreamlitFunctions.print_tax_brackets()
StreamlitFunctions.reset_tax_brackets()

StreamlitFunctions.print_salary_parameters()
StreamlitFunctions.reset_salary_parameters()
st.button(
    "Calculate Based on Salary Parameters",
    use_container_width=True,
    on_click=calculate_salary_parameters,
)

StreamlitFunctions.initial_salary_parameter()
StreamlitFunctions.reset_initial_salary_parameter()
st.button(
    "Calculate Based on Desired Net Salary",
    use_container_width=True,
    on_click=calculate_initial_salary_parameter,
)

StreamlitFunctions.print_tax_on_current_salary()
StreamlitFunctions.reset_tax_on_current_salary()
st.button(
    "Calculate Tax on Current Salary",
    use_container_width=True,
    on_click=calculate_tax_on_current_salary,
)

if st.session_state.type_to_calculate is not None:
    if st.session_state.type_to_calculate == "tax_on_current_salary":
        initial_desired_net = Functions.calculated_current_salary_after_tax(
            st.session_state.tax_on_current_salary, st.session_state.tax_brackets
        )
    elif st.session_state.type_to_calculate == "desired_salary":
        initial_desired_net = st.session_state.user_initial_desired_net
    elif st.session_state.type_to_calculate == "salary_parameters":
        initial_desired_net = Functions.calculated_initial_desired_net(
            st.session_state.current_salary,
            st.session_state.desired_increment_percentage,
            st.session_state.daily_cost_of_travel,
            st.session_state.physical_days_per_week,
        )

    result = Functions.calculate_additional_amount(
        initial_desired_net, st.session_state.tax_brackets
    )

    # Display how initial_desired_net was determined
    st.markdown("---")
    if st.session_state.type_to_calculate == "tax_on_current_salary":
        st.success(
            "✅ Calculation was done based on the selected value of 'Tax on Current Salary'"
        )
        summary_df = pd.DataFrame(
            {
                "Parameter": [
                    "Current Salary",
                    "Tax",
                    "Gross Salary",
                ],
                "Value": [
                    f"PKR {result['final_net_salary']:,.2f}",
                    f"PKR {result['tax']:,.2f}",
                    f"PKR {result['gross_salary_needed']:,.2f}",
                ],
            }
        )
    elif st.session_state.type_to_calculate == "desired_salary":
        st.success(
            "✅ Calculation was done based on the selected value of 'Final Desired Net Salary'"
        )
        summary_df = pd.DataFrame(
            {
                "Parameter": [
                    "Final Net Salary",
                    "Tax",
                    "Gross Salary",
                ],
                "Value": [
                    f"PKR {result['final_net_salary']:,.2f}",
                    f"PKR {result['tax']:,.2f}",
                    f"PKR {result['gross_salary_needed']:,.2f}",
                ],
            }
        )
    elif st.session_state.type_to_calculate == "salary_parameters":
        st.success(
            "✅ Calculation was done based on the selected values of 'Salary Parameters'"
        )
        summary_df = pd.DataFrame(
            {
                "Parameter": [
                    "Current Salary",
                    "Desired Increment",
                    "Daily Travel Cost",
                    "On-Site Days/Week",
                    "Gross Salary",
                    "Tax",
                    "Final Net Salary",
                ],
                "Value": [
                    f"PKR {st.session_state.current_salary:,.2f}",
                    f"{st.session_state.desired_increment_percentage:.2%}",
                    f"PKR {st.session_state.daily_cost_of_travel:,.2f}",
                    f"{st.session_state.physical_days_per_week}",
                    f"PKR {result['gross_salary_needed']:,.2f}",
                    f"PKR {result['tax']:,.2f}",
                    f"PKR {result['final_net_salary']:,.2f}",
                ],
            }
        )
    st.header("Salary Calculation Results")
    col1, col2 = st.columns(2)
    with col1:
        # custom_metric("Initial Desired Net Salary", result['initial_desired_net'])
        StreamlitFunctions.custom_metric("Final Net Salary", result["final_net_salary"])
        StreamlitFunctions.custom_metric("Tax", result["tax"])

    with col2:
        # custom_metric("Additional Amount Needed", result['additional_amount'])
        StreamlitFunctions.custom_metric(
            "Gross Salary Needed", result["gross_salary_needed"]
        )
    # Display a summary of the calculation
    st.subheader("Calculation Summary")
    st.data_editor(summary_df, use_container_width=True, hide_index=True)
    st.session_state.type_to_calculate = None

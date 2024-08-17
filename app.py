import streamlit as st

from functions import Functions, StreamlitFunctions
import pandas as pd

StreamlitFunctions.initialize_session_values()
StreamlitFunctions.print_tax_brackets()
StreamlitFunctions.reset_tax_brackets()

StreamlitFunctions.print_salary_parameters()
StreamlitFunctions.reset_salary_parameters()

StreamlitFunctions.initial_salary_parameter()
StreamlitFunctions.reset_initial_salary_parameter()
StreamlitFunctions.check_initial_salary_parameter()

if st.button("Calculate", use_container_width=True) and st.session_state.valid_input:
    if st.session_state.user_initial_desired_net > 0:
        initial_desired_net = st.session_state.user_initial_desired_net
    else:
        initial_desired_net = Functions.calculated_initial_desired_net(
            st.session_state.current_salary,
            st.session_state.desired_increment_percentage,
            st.session_state.daily_cost_of_travel,
            st.session_state.physical_days_per_week,
        )

    result = Functions.calculate_additional_amount(
        initial_desired_net, st.session_state.tax_brackets
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

    # Display how initial_desired_net was determined
    st.markdown("---")
    if st.session_state.user_initial_desired_net > 0:
        st.success("✅ Initial Desired Net Salary was provided by the user.")
    else:
        st.info(
            "ℹ️ Initial Desired Net Salary was calculated based on the provided parameters."
        )

    # Display a summary of the calculation
    st.subheader("Calculation Summary")
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
    st.table(summary_df)

    st.subheader("Salary Breakdown")
    breakdown_data = {
        "Component": ["Net Salary", "Tax"],
        "Amount": [result["final_net_salary"], result["tax"]],
    }
    breakdown_df = pd.DataFrame(breakdown_data)
    st.bar_chart(breakdown_df.set_index("Component"))

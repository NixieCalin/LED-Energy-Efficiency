
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="LED vs Incandescent Efficiency",
    page_icon="💡",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("💡 Project Menu")

selected_page = st.sidebar.radio(
    "Navigate to",
    ["Dashboard", "Data Overview", "Visual Analysis", "About Project"]
)

st.sidebar.divider()
st.sidebar.info("LED vs Incandescent Energy Efficiency")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_dataset.csv")

df = load_data()

# Calculate average values
led = df[df["bulb_type"] == "LED"].mean(numeric_only=True)
incandescent = df[
    df["bulb_type"] == "Incandescent"
].mean(numeric_only=True)

# ---------------------------------
# PAGE 1: DASHBOARD
# ---------------------------------
if selected_page == "Dashboard":

    st.title("💡 LED vs Incandescent Energy Efficiency")
    st.write(
        "A comparison of energy consumption, lighting efficiency, "
        "electricity cost, and carbon emissions."
    )

    st.success("Dataset loaded successfully!")

    st.subheader("LED vs Incandescent Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average LED Power",
            f"{led['power_rating_watts']:.2f} W",
            f"{incandescent['power_rating_watts'] - led['power_rating_watts']:.2f} W lower"
        )

    with col2:
        st.metric(
            "Average LED Efficiency",
            f"{led['luminous_efficacy_lumens_per_watt']:.2f} lm/W"
        )

    with col3:
        st.metric(
            "Average LED Brightness",
            f"{led['measured_brightness_lumens']:.2f} lm"
        )

    st.subheader("Annual Impact Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "LED Annual Energy",
            f"{led['annual_energy_consumption_kwh']:.2f} kWh",
            f"{incandescent['annual_energy_consumption_kwh'] - led['annual_energy_consumption_kwh']:.2f} kWh saved"
        )

    with col2:
        st.metric(
            "LED Annual Electricity Cost",
            f"₹{led['estimated_annual_electricity_cost_inr']:.2f}",
            f"₹{incandescent['estimated_annual_electricity_cost_inr'] - led['estimated_annual_electricity_cost_inr']:.2f} saved"
        )

    with col3:
        st.metric(
            "LED Annual CO₂ Emissions",
            f"{led['estimated_annual_co2_emissions_kg']:.2f} kg",
            f"{incandescent['estimated_annual_co2_emissions_kg'] - led['estimated_annual_co2_emissions_kg']:.2f} kg lower"
        )

    st.divider()

    st.subheader("Interactive Bulb Comparison")

    metric_options = {
        "Power Consumption (Watts)": "power_rating_watts",
        "Brightness (Lumens)": "measured_brightness_lumens",
        "Luminous Efficacy (Lumens/Watt)": "luminous_efficacy_lumens_per_watt",
        "Annual Energy (kWh)": "annual_energy_consumption_kwh",
        "Annual Electricity Cost (INR)": "estimated_annual_electricity_cost_inr",
        "Annual CO₂ Emissions (kg)": "estimated_annual_co2_emissions_kg"
    }

    selected_metric = st.selectbox(
        "Choose a metric to compare",
        list(metric_options.keys())
    )

    metric_column = metric_options[selected_metric]

    comparison = df.groupby("bulb_type")[metric_column].mean()

    st.bar_chart(comparison)

    st.caption(
        "The chart displays average values calculated from the dataset."
    )    
    st.divider()

    st.subheader("Key Findings")

    st.write("""
    - LED bulbs provide approximately similar average brightness
      while consuming significantly less power.
    - LED bulbs show approximately 6.39 times higher average
      luminous efficacy.
    - Average annual energy consumption is approximately 85.92%
      lower for LED bulbs.
    - Estimated annual electricity cost is reduced by approximately
      85.92%.
    - Estimated annual CO₂ emissions are approximately 85.92%
      lower for LED bulbs.
    """)

    st.caption(
        "Findings are based on dataset averages and the stated assumptions."
    )
# ---------------------------------
# PAGE 2: DATA OVERVIEW
# ---------------------------------
elif selected_page == "Data Overview":

    st.title("📊 Data Overview")

    st.write("### Dataset Information")
    st.write(f"Total records: {len(df)}")
    st.write(f"Total columns: {len(df.columns)}")

    # Interactive bulb type filter
    st.subheader("Filter Dataset")

    selected_bulbs = st.multiselect(
        "Select bulb types",
        options=df["bulb_type"].unique(),
        default=df["bulb_type"].unique()
    )

    filtered_df = df[df["bulb_type"].isin(selected_bulbs)]

    st.write(f"Showing {len(filtered_df)} records")

    # Filtered bulb distribution
    st.write("### Bulb Type Distribution")

    if not filtered_df.empty:
        st.bar_chart(filtered_df["bulb_type"].value_counts())
        st.write("### Filtered Dataset")
        st.dataframe(filtered_df, use_container_width=True)

        csv_data = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Filtered Dataset",
            data=csv_data,
            file_name="filtered_bulb_data.csv",
            mime="text/csv"
        )

    else:
        st.warning("Please select at least one bulb type.")


# ---------------------------------
# PAGE 3: VISUAL ANALYSIS
# ---------------------------------
elif selected_page == "Visual Analysis":

    st.title("📈 Visual Analysis")

    st.write(
        "Visual comparison of LED and incandescent bulbs "
        "based on the dataset."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Annual Energy Consumption")
        st.image("outputs/annual_energy_comparison.png",
                 use_container_width=True)

    with col2:
        st.write("### Luminous Efficacy")
        st.image("outputs/luminous_efficacy_comparison.png",
                 use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.write("### Annual CO₂ Emissions")
        st.image("outputs/co2_emissions_comparison.png",
                 use_container_width=True)

    with col4:
        st.write("### Annual Electricity Cost")
        st.image("outputs/electricity_cost_comparison.png",
                 use_container_width=True)

    st.write("### Brightness vs Power Consumption")
    st.image("outputs/brightness_vs_power.png",
             use_container_width=True)

# ---------------------------------
# PAGE 4: ABOUT PROJECT
# ---------------------------------
elif selected_page == "About Project":

    st.title("ℹ️ About the Project")

    st.subheader("Objective")
    st.write(
        "To compare LED and incandescent bulbs based on lighting "
        "efficiency, energy consumption, electricity cost, "
        "and estimated carbon emissions."
    )

    st.subheader("Methodology")
    st.write(
        "Existing datasets were collected and validated. "
        "The data were cleaned, and energy consumption, "
        "luminous efficacy, electricity cost, and carbon "
        "emissions were calculated using Python."
    )

    st.subheader("Key Formulas")

    st.latex(r"Luminous\ Efficacy = \frac{Brightness\ (lumens)}{Power\ (watts)}")

    st.latex(r"Annual\ Energy\ (kWh) = \frac{Power\ (W) \times Hours/day \times 365}{1000}")

    st.subheader("Assumptions")
    st.write(
        "- Electricity tariff: Dataset-assumed ₹8 per kWh.\n"
        "- Grid emission factor: Dataset-assumed value.\n"
        "- Annual usage is estimated using the daily usage hours "
        "provided in the dataset.\n"
        "- Results are based on existing datasets, not physical "
        "bulb experiments."
    )

    st.subheader("Conclusion")
    st.write(
        "The dataset averages indicate that LED bulbs provide "
        "similar brightness while consuming less power than "
        "incandescent bulbs. They also show lower estimated "
        "annual electricity costs and carbon emissions."
    )

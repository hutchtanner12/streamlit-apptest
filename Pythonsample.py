import streamlit as st
import matplotlib.pyplot as plt

# Title of the app
st.title('Lyft Pricing Optimization Dashboard')

# User inputs
lyft_take = st.slider('Lyft’s Take per Ride ($)', min_value=0, max_value=10, value=3)
driver_payout = st.number_input('Driver Payout per Ride ($)', min_value=0, value=19)
ride_rate = 25
match_rate = 0.93

# Calculations
revenue_per_ride = ride_rate - lyft_take
net_revenue_per_ride = revenue_per_ride - driver_payout

rides_requested = 1000
rides_completed = rides_requested * match_rate

total_revenue = rides_completed * revenue_per_ride
total_payout = rides_completed * driver_payout
net_revenue = total_revenue - total_payout

# Display results
st.write(f'Net Revenue per Ride: ${net_revenue_per_ride:.2f}')
st.write(f'Total Monthly Revenue: ${total_revenue:.2f}')
st.write(f'Total Monthly Payout: ${total_payout:.2f}')
st.write(f'Total Monthly Net Revenue: ${net_revenue:.2f}')

# Plotting
fig, ax = plt.subplots()
ax.plot([lyft_take], [net_revenue], 'ro', label='Net Revenue')
ax.set_xlabel('Lyft’s Take ($)')
ax.set_ylabel('Net Revenue ($)')
ax.set_title('Net Revenue vs Lyft’s Take')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

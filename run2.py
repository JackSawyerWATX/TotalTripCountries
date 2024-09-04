
# TODO: Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["Ireland", "Luxembourg", "Belgum", "Switzerland"]

# TODO: Define a dictionary named country_fuel_costs with fuel costs for countries
country_fuel_costs = {"Ireland": 45, "Luxembourg": 65, "Belgum": 50, "Switzerland":75}

# TODO: Initialize a variable total_fuel_cost to 0
total_fuel_cost = 0

# TODO: Use a for loop to add up the fuel cost for each chosen country
for country in chosen_countries:
    total_fuel_cost += country_fuel_costs[country]

# TODO: Calculate the average fuel cost per country
average_fuel_cost = total_fuel_cost / len(chosen_countries)

# TODO: Print the total fuel cost for the road trip
print(f"The total fuel cost for the trip should be €{total_fuel_cost:.2f}")

# TODO: Print the average fuel cost per country
print(f"The average fuel cost for the trip should be €{average_fuel_cost:.2f}")
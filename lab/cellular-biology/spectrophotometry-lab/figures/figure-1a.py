x = [0.00125, 0.0125, 0.125, 0.25, 0.50, 1.00] # Molarity (Concentration)
y = [0.001, 0.02, 0.026, 0.061, 0.095, 0.218] # Absorbance

# Convert x to a NumPy array and reshape it
x = np.array(x).reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Predict values
y_pred = model.predict(x)

# Create scatter plot
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the linear regression line
plt.plot(x, y_pred, color='lightgrey', label='Linear Regression Line')

# Add labels and title
plt.title("Spectrophotometry Lab")
plt.xlabel("Concentration (M)")
plt.ylabel("Absorbance")
plt.legend()

# Print the equation of the line
slope = model.coef_[0]
intercept = model.intercept_

# Calculate and print the R^2 value
r_squared = model.score(x, y)

# Add text to the plot with reduced space
equation_text = f"y = {slope:.3f}x + {intercept:.5f}"
r_squared_text = f"R^2 = {r_squared:.3f}"

# Get the axis limits
x_limits = plt.gca().get_xlim()
y_limits = plt.gca().get_ylim()

# Calculate positions for the text based on the axis limits
x_text_position = x_limits[0] + (x_limits[1] - x_limits[0]) * 0.035
y_text_position = y_limits[1] - (y_limits[1] - y_limits[0]) * 0.075

plt.text(x_text_position, y_text_position, equation_text, fontsize=12, color='blue')
plt.text(x_text_position, y_text_position - (y_limits[1] - y_limits[0]) * 0.075, r_squared_text, fontsize=12, color='blue')

# Show the plot
plt.show()
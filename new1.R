# R code for a basic data visualization
# This code generates a scatter plot using random data

# Set a seed for reproducibility
set.seed(123)

# Generate random data
num_points <- 50
x <- rnorm(num_points)
y <- 2 * x + rnorm(num_points)


plot(x, y, main = "Scatter Plot of X and Y",
     xlab = "X-axis", ylab = "Y-axis",
     pch = 16, col = "blue")

# Add a regression line
abline(lm(y ~ x), col = "red")
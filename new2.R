# R code for a simple calculation
# This code adds two numbers and prints the result

# Function to add two numbers
add_numbers <- function(x, y) {
  result <- x + y
  return(result)
}

# Test the function with sample values
num1 <- 5
num2 <- 7
result <- add_numbers(num1, num2)

# Print the result
cat("The sum of", num1, "and", num2, "is", result, "\n")
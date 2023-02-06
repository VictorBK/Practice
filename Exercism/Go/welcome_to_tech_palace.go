package techpalace

import ("fmt"
		"strings")

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
		fmt.Println("Welcome to the Tech Palace, " + strings.ToUpper(customer))

		return "Welcome to the Tech Palace, " + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
		stars := strings.Repeat("*", numStarsPerLine)

		fmt.Println(stars + "\n" + welcomeMsg + "\n" + stars)

		return stars + "\n" + welcomeMsg + "\n" + stars
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
		fmt.Println(strings.Trim(strings.TrimSpace(strings.ReplaceAll(oldMsg, "*", "")), "\n"))

		return strings.Trim(strings.TrimSpace(strings.ReplaceAll(oldMsg, "*", "")), "\n")
}


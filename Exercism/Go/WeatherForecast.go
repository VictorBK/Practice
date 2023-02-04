// Package weather provides basic weather-related information.
package weather

// CurrentCondition variable presents the current weather condition.
var CurrentCondition string

// CurrentLocation represents the location of the current weather forecast.
var CurrentLocation string

// Forecast returns a string that describes the weather conditions for the location provided.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}

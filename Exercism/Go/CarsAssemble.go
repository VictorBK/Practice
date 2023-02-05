package cars

// CalculateWorkingCarsPerHour calculates how many cares are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
		var ans float64
	var t float64 = float64(productionRate)
	ans = t * successRate / 100
	return ans

}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
		var ans int
	var r float64
	var t float64 = float64(productionRate)
	r = t * successRate / 100
	ans = int(r / 60)
	return ans
}

// CalculateCost works out the cost of producing a given number of cars.
func CalculateCost(carsCount int) uint {
	var rem, q, ans int
	var r uint
	rem = carsCount % 10
	q = carsCount / 10
	ans = q * 95000 + rem * 10000
	r = uint(ans)
	return r
}
package main

import (
	"fmt"
	"math"
)

// time value of money
func futureValueOfMoneyDiscrete(amount int, rate int, years int) float32 {
	ratePercent := float64(rate) / 100
	denominator := math.Pow(float64(1+ratePercent), float64(years))
	return float32(amount) * float32(denominator)
}

func futureValueOfMoneyContinuous(amount int, rate int, years int) float32 {
	rateByHundered := float32(rate) / 100
	return float32(amount) * float32(math.Exp(float64(rateByHundered)*float64(years)))
}

// modern portfolio theory

func main() {
	fmt.Println("hello")
	y := futureValueOfMoneyContinuous(100, 5, 3)
	z := futureValueOfMoneyDiscrete(100, 5, 3)
	fmt.Println(y)
	fmt.Println(z)
}

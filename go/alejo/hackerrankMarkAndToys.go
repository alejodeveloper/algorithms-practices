package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Complete the maximumToys function below.
func maximumToys(prices []int, budget int) int {
	boughtToys := 0
	moneyExpended := 0

	for _, toy := range prices {
		if moneyExpended + toy <= budget {
			moneyExpended += toy
			boughtToys ++
		} else {
			break
		}
	}

	return boughtToys
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	myCheckError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	nk := strings.Split(myReadLine(reader), " ")

	nTemp, err := strconv.ParseInt(nk[0], 10, 64)
	myCheckError(err)
	numberOfToys := int32(nTemp)

	kTemp, err := strconv.ParseInt(nk[1], 10, 64)
	myCheckError(err)
	budget := int(kTemp)

	pricesTemp := strings.Split(myReadLine(reader), " ")

	var prices []int

	for i := 0; i < int(numberOfToys); i++ {
		pricesItemTemp, err := strconv.ParseInt(pricesTemp[i], 10, 64)
		myCheckError(err)
		pricesItem := int(pricesItemTemp)
		prices = append(prices, pricesItem)
	}
	sort.Ints(prices)
	result := maximumToys(prices, budget)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func myReadLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func myCheckError(err error) {
	if err != nil {
		panic(err)
	}
}

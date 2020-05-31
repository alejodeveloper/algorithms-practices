package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the countingValleys function below.
func countingValleys(_ int, steps string) int {
	myStepsCount := 0
	valleys := 0
	for _, step := range steps {
		if string(step) == "U" {
			if myStepsCount == -1 {
				valleys += 1
			}
			myStepsCount ++
		} else {
			myStepsCount --
		}
	}

	return valleys
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	myCheckError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	myCheckError(err)
	n := int(nTemp)

	s := myReadLine(reader)

	result := countingValleys(n, s)

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

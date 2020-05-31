package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the contacts function below.
 */

var myResults =  map[string] int {}

func contacts(contact string) {
	for index, _ := range contact {
		myContact := string(contact[0:index+1])
		myResults[myContact] += 1
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()
	writer := bufio.NewWriterSize(stdout, 1024 * 1024)
	queriesRows, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)

	for queriesRowItr := 0; queriesRowItr < int(queriesRows); queriesRowItr++ {
		queriesRowTemp := strings.Split(readLine(reader), " ")

		var queriesRow []string
		for _, queriesRowItem := range queriesRowTemp {
			queriesRow = append(queriesRow, queriesRowItem)
		}

		if len(queriesRow) != int(2) {
			panic("Bad input")
		}
		if queriesRow[0] == "add" {
			contacts(queriesRow[1])
		} else {
			fmt.Fprintf(writer ,"%d", myResults[queriesRow[1]])
			fmt.Fprintf(writer ,"\n")
		}
	}
	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

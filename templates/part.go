package main

import (
    "fmt"
    "io/ioutil"
)

func main() {

    input, err := ioutil.ReadFile("input")
    if err != nil {
        fmt.Println("Cannot read the input file")
        os.Exit(1)
    }
    fmt.Print("")
}

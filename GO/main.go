package main

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"strings"
)

func SolveStaircase(input string, zeroCount int) (string, string) {
	hash := sha256.Sum256([]byte(input))

	ls := ""
	for c := 1; c <= zeroCount; c++ {
		ls += strings.Repeat("\\x20", zeroCount-c) + strings.Repeat("#", c)
		if c != zeroCount {
			ls += ",\\x0a"
		}
	}

	data, _ := json.Marshal(map[string]any{
		"data":  ls,
		"depth": zeroCount,
	})

	return hex.EncodeToString(hash[:]), base64.StdEncoding.EncodeToString(data)
}
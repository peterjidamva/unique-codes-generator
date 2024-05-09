package generator

import (
	"fmt"
	"github.com/sony/sonyflake"
	"log"
	"runtime"
	"time"
)

func GenIdWithSonyFlake() (string, error) {
	flake := sonyflake.NewSonyflake(sonyflake.Settings{})
	id, err := flake.NextID()
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("%v", id), err
}

func GenIdsWithSonyFlake(count int32) ([]string, error) {

	// Figure out how many CPUs are available and tell Go to use all of them
	numThreads := int32(runtime.NumCPU())
	runtime.GOMAXPROCS(int(numThreads))

	allCodes := make([]string, 0, numThreads)

	var countPerThread = count / numThreads
	ch := make(chan []string)

	threads := make([][]string, numThreads)

	startRun := time.Now()

	for j := 0; j < int(numThreads); j++ {

		go func() {
			codes := make([]string, 0, numThreads)
			var i int32
			for i = 0; i <= countPerThread-1; i++ {
				code, err := GenIdWithSonyFlake()
				if err != nil {
					log.Fatalf("%v", err)
				}
				codes = append(codes, code)
			}
			ch <- codes
		}()

	}

	for i := 0; i < int(numThreads); i++ {
		threads[i] = <-ch
	}

	fmt.Printf("%v", threads)

	elapsedRun := time.Since(startRun)
	fmt.Printf("Multi-threaded run took %s\n", elapsedRun)

	return allCodes, nil
}

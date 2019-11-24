prog3: dna.o dnadriver.o
	g++ -o prog3 dna.o dnadriver.o

clean:
	/bin/rm -f *.o prog3

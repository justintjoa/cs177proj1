DNA: dna.o dnadriver.o
	g++ -o DNA dna.o dnadriver.o

clean:
	/bin/rm -f *.o DNA

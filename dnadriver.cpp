#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atof */
#include <math.h> 
#include <string>
#include <string.h>
#include <algorithm>
#include "dna.h"
using namespace std;

int main(int argc, char* argv[])
{
    double m = 2;
    double c = -0.5;
    double d = -1;
    string a;
    string b;
    bool score = false;
    bool change = false;
    bool erase = false;
    bool stringone = false;
    bool stringtwo = false;
    bool hadonestring = false;
    bool hadtwostring = false;
    for(int i=0; i<argc; i++) {   
    	if (score == true) {
    		m = stod(argv[i]);
    		score = false;
    		continue;
    	}
    	if (change == true) {
    		c = atof(argv[i]);
    		change = false;
    		continue;
    	}
    	if (erase == true) {
    		d = atof(argv[i]);
    		erase = false;
    		continue;
    	}
    	if (stringone == true) {
    		hadonestring = true;
    		std::ifstream ifs(argv[i]);
    		a = string((std::istreambuf_iterator<char>(ifs)),
                  (std::istreambuf_iterator<char>()));
			a.erase(std::remove(a.begin(), a.end(), '\n'), a.end());
    		stringone = false;
    		continue;
    	}
    	if (stringtwo == true) {
    		hadtwostring = true;
    		std::ifstream ifs(argv[i]);
    		b = string((std::istreambuf_iterator<char>(ifs)),
                  (std::istreambuf_iterator<char>()));
    		b.erase(std::remove(b.begin(), b.end(), '\n'), b.end());
    		stringtwo = false;
    		continue;
    	}
    	if (strcmp(argv[i],"-m") == 0) {
    		score = true;
    		continue;
    	}
    	if (strcmp(argv[i],"-c") == 0) {
    		change = true;
    		continue;
    	}
    	if (strcmp(argv[i],"-d") == 0) {
    		erase = true;
    		continue;
    	}
    	if (strcmp(argv[i],"-1") == 0) {
    		stringone = true;
    		continue;
    	}
    	if (strcmp(argv[i],"-2") == 0) {
    		stringtwo = true;
    		continue;
    	}
    	
    }
    if ((score == true) || (erase == true) || (change == true) || (stringone == true) || (stringtwo == true)) {
    	cout << "invalid input" << endl;
    	return 0;
    }
    if (!((hadonestring == true) && (hadtwostring == true))) {
    	cout << "invalid input" << endl;
    	return 0;
    }
	DNAreader k(a,b,m,c,d);
	// string f1 = "CTGGGCTAAAAGGTCCCTTAGCCTATTTAGAAAAATGGGCCATTAGGAAATTGCAAGGAAGAACCATTCGTGAGAGGGATTAGCTGAGCTCTTTTGACTCTCTAATCACCCCTCCGTGCT";
 //    string f2 = "CCTCACCTGAAGTGTCCAGCAAATACACCAAGGGTGACGCAGGACAAGCATGAGCCATTCATACTGCTGCAACCAGAGAGAGGGAGCAGGAAAATGAGACAGGGAGGGGGCCAAAT";
 //    DNAreader T(f1,f2,2,-1,-2);
    return 0;
}


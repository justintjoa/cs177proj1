#include <iostream>
#include <vector>
#include <cstring>
#include <string.h> 
#include <iomanip>
#include <algorithm>
#include <algorithm>
#include <string>
#include <stdio.h>
#include "dna.h"
using namespace std;

	DNAreader::DNAreader(string a, string b, double m, double c, double d) {
		c = -c;
		d = -d;
		if ((strcmp(a.c_str(),"") == 0) && (strcmp(b.c_str(),"") == 0)) {
			cout << 0 << endl;
			return;
		}
		if (strcmp(a.c_str(),"") == 0) {
			double product;
			product = -d*(b.size());
			cout << product << endl;
			return;
		}
		if (strcmp(b.c_str(),"") == 0) {
			double product;
			product = -d*(a.size());
			cout << product << endl;
			return;
		}
		similarity = 0;
		collection.push_back(a);
		collection.push_back(b);
		int height = b.size();
		int width = a.size();
		double chart[height][width];
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				chart[i][j] = 0;
			}
		}
		double cost1 = -c;
		double cost2 = -2*d;
		double finalcost = max(cost1,cost2);
		char origin;
		origin = a.at(0);
		for (int i = 0; i < b.size(); i++) {
			// cout << (b.at(i)) << " bews" << endl;
			// cout << origin << endl;
			if ((b.at(i)) == origin) {
				if (i != 0) {
					chart[0][0] = finalcost;
					chart[i][0] = m + c;
					break;
				}
				chart[i][0] = m;
				break;
			}
		}
		origin = b.at(0);
		for (int i = 0; i < a.size(); i++) {
			// cout << (a.at(i)) << " cews" << endl;
			// cout << origin << endl;
			if ((a.at(i)) == origin) {
				chart[0][i] = m;
				if (i != 0) {
					chart[0][i] = chart[0][i] + c;
				}
				break;
			}
		}
		// for (int i = 0; i < height; i++) {
		// 	for (int j = 0; j < width; j++) {
		// 		cout << chart[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }
		for (int i = 1; i < width; i++) {
			chart[0][i] = chart[0][i-1] + chart[0][i] - d;
		}
		for (int i = 1; i < height; i++) {
			chart[i][0] = chart[i-1][0] + chart[i][0] - d;
		}
		// for (int i = 0; i < height; i++) {
		// 	for (int j = 0; j < width; j++) {
		// 		cout << chart[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }
		for (int i = 1; i < height; i++) {
			for (int j = 1; j < width; j++) {
				double cost;
				cost = finalcost;
				if (a.at(j) == b.at(i)) {
					cost = m;
				}
				double diagonal;
				diagonal = chart[i-1][j-1] + cost;
				double notdiagonal;
				notdiagonal = max(chart[i][j-1]-d,chart[i-1][j]-d);
				chart[i][j] = max(diagonal,notdiagonal);
				continue;
			}
		}
		// for (int i = 0; i < height; i++) {
		// 	for (int j = 0; j < width; j++) {
		// 		cout << chart[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }
		// cout << "result is" << endl;
		cout << std::setprecision(4) << chart[height-1][width-1] << endl;
		// cout << "done" << endl;
	}

	DNAreader::~DNAreader() {

	}

	






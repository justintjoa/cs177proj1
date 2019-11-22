#include <iostream>
#include <vector>
#include <cstring>
#include <string.h> 
#include <iomanip>
#include <algorithm>
#include "dna.h"
using namespace std;

	DNAreader::DNAreader(string a, string b, double m, double c, double d) {
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
				break;
			}
		}
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				cout << chart[i][j] << " ";
			}
			cout << endl;
		}
		for (int i = 1; i < width; i++) {
			chart[0][i] = chart[0][i-1] + chart[0][i] - d;
		}
		for (int i = 1; i < height; i++) {
			chart[i][0] = chart[i-1][0] + chart[i][0] - d;
		}
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				cout << chart[i][j] << " ";
			}
			cout << endl;
		}
		for (int i = 1; i < height; i++) {
			for (int j = 1; j < width; j++) {
				double value1 = chart[i-1][j];
				double value2 = chart[i-1][j-1];
				double value3 = chart[i][j-1];
				double finalvalue = max(value1,value2);
				finalvalue = max(finalvalue,value3);
				int previousheight = 0;
				int previouswidth = 0;
				int previousdimension = 0;
				if (finalvalue == value1) {
					previousheight = i-1;
					previouswidth = j;
				}
				if (finalvalue == value2) {
					previousheight = i-1;
					previouswidth = j-1;
				}
				if (finalvalue == value3) {
					previousheight = i;
					previouswidth = j-1;
				}
				previousdimension = min(previousheight,previouswidth);
				int extra1;
				int extra2;
				extra1 = i - previousdimension;
				extra2 = j - previousdimension;
				if (a.at(j) != b.at(i)) {
					if (extra1 == extra2) {
						double diagonal = finalcost + finalvalue;
						chart[i][j] = diagonal;
					}
					if (extra1 != extra2) {
						double notdiagonal;
						notdiagonal = finalvalue - d;
						chart[i][j] = notdiagonal;
					}
					continue;
				}
				if (a.at(j) == b.at(i)) {
					if (extra1 == extra2) {
						chart[i][j] = finalvalue + m;
					}
					if (extra1 != extra2) {
						double include;
						double noinclude;
						include = chart[i-1][j-1] + m;
						noinclude = finalvalue - d;
						chart[i][j] = max(include,noinclude);
					}
					continue;
				}
			}
		}
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				cout << chart[i][j] << " ";
			}
			cout << endl;
		}
		cout << "done" << endl;
	}

	DNAreader::~DNAreader() {

	}

	






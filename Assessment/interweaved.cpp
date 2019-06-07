#include<iostream>
using namespace std;

bool isLarger(string str1, string str2) {
	return str1.length() > str2.length();
}

string interweaved(string str1, string str2) {
	string ans = "";

	for (int i = 0; i < (str1.length() > str2.length() ? str2.length() : str1.length()); i++) {
			ans.append(str1.charAt(i));
			ans.append(str2.charAt(i));
	}

	if (isLarger(str1, str2)) {
		for (int i = str2.length(); i < str1.length(); i++)
			ans.append(str1.charAt(i));
	}

	else {
		for (int i = str1.length(); i < str2.length(); i++)
			ans.append(str2.charAt(i));
	}

	return ans;
}


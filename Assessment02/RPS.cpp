#include <iostream>
using namespace std;

int winner(string games) {
			if(games[0] == 'P' && games[1] == 'S')
				return 2;
			else if(games[0] == 'S' && games[1] == 'P')
				return 1;
			else if(games[0] == 'R' && games[1] == 'S')
				return 1;
			else if(games[0] == 'S' && games[1] == 'R')
				return 2;
			else if(games[0] == 'R' && games[1] == 'P')
				return 2;
			else if(games[0] == 'P' && games[1] == 'R')
				return 1;
		
		return 0;
	}
	
	string RockPaperScissors(string games) {
		string ans = "";
		int winner1 = 0;
		int winner2 = 0;
		int draw = 0;
		for (int i = 0 ; i < games.length(); i = i + 3) {
			if (winner(games[i, i + 1]) == 1)
				winner1++;
			else if (winner(games[i, i + 1]) == 2)
				winner2++;
			else
				draw++;
		}
		
		ans.append("+" , winner1, ", -", winner2, ", " , draw);
		
		return ans;
	}

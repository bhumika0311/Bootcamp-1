	public static int winner(String games) {
			if(games.charAt(0) == 'P' && games.charAt(1) == 'S')
				return 2;
			else if(games.charAt(0) == 'S' && games.charAt(1) == 'P')
				return 1;
			else if(games.charAt(0) == 'R' && games.charAt(1) == 'S')
				return 1;
			else if(games.charAt(0) == 'S' && games.charAt(1) == 'R')
				return 2;
			else if(games.charAt(0) == 'R' && games.charAt(1) == 'P')
				return 2;
			else if(games.charAt(0) == 'P' && games.charAt(1) == 'R')
				return 1;
		
		return 0;
	}
	
	public static String RockPaperScissors(String games) {
		String ans = "";
		int winner1 = 0;
		int winner2 = 0;
		int draw = 0;
		for (int i = 0 ; i < games.length(); i = i + 3) {
			if (winner(games.substring(i, i + 1)) == 1)
				winner1++;
			else if (winner(games.substring(i, i + 1)) == 2)
				winner2++;
			else
				draw++;
		}
		
		ans += "+" + winner1 + ", -" + winner2 + ", " + draw;
		
		return ans;
	}
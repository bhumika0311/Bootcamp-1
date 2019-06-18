class isPangram {

	public static Boolean isPangram(String s) {
		char alphabets = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
				'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
		char frequency = new int[26];
		for (int i = 0; i < 26; i++) {
			for (int j = 0; j < s.length(); j++) {
				if (alphabets[i] == s.charAt(j)) {
					frequency[i]++;
				}
			}

		}
		
		for (int i = 0; i < 26; i++) {
			if (frequency[i] == 0)
				return false;
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		System.out.println(isPangram("The quick brown x jumps over the lazy dog"));
	}
}
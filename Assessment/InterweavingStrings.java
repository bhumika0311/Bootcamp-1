
public class InterweavingStrings {

	public static boolean isLarger(String str1, String str2) {
		return str1.length() > str2.length();
	}

	public static String interweaved(String str1, String str2) {
		String ans = "";

		for (int i = 0; i < (str1.length() > str2.length() ? str2.length() : str1.length()); i++) {
			ans += str1.charAt(i);
			ans += str2.charAt(i);
		}

		if (isLarger(str1, str2)) {
			for (int i = str2.length(); i < str1.length(); i++)
				ans += str1.charAt(i);
		}

		else {
			for (int i = str1.length(); i < str2.length(); i++)
				ans += str2.charAt(i);
		}

		return ans;
	}

	public static void main(String args[]) {
		System.out.print(interweaved("Bhumika", "Saxena"));
	}

}

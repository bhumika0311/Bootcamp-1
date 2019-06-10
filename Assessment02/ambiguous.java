package Assignment2June;

public class ambiguous {

	public static int convertToInteger(String str1) {
		return Integer.parseInt(str1);
	}

	public static Boolean isAmbiguous(String str1) {
		return convertToInteger(str1.substring(0, 2)) <= 12 && convertToInteger(str1.substring(3, 5)) <= 12;

	}

	public static void main(String args[]) {
		System.out.println(isAmbiguous("12/11/2018"));
		System.out.println(isAmbiguous("11/02/2018"));
		System.out.println(isAmbiguous("30/11/2018"));
		System.out.println(isAmbiguous("11/31/2018"));
	}

}


public class Triplets {
	
	public static boolean  isTriplet(int number1, int number2, int number3) {
		return (Math.pow(number1, 3) + Math.pow(number2, 3) == Math.pow(number3, 2));
	}
	
	public static String firstTenTriplets() {
		int number1 = 1;
		int number2 = 2; 
		int number3 = 3;
		String answer = "";
		int count = 0;
		while(count <= 10) {
			if(isTriplet(number1, number2, number3)) {
				answer += number1 + "," + number2 + "," + number3 + " ";
				count++;
			}
			if(numberToIncrement(number1, number2, number3) == 1) 
				number1++;
			else if(numberToIncrement(number1, number2, number3) == 2)
				number2++;
			else
				number3++;
		}
		return answer;
	}
	
	///////////////////////////
	
	public static int numberToIncrement(int number1, int number2, int number3) {
		if(number2 - number1 == 2)
			return 1;
		else if (number3 - number2 == 1)
			return 3;
		else
			return 2;
	}

}

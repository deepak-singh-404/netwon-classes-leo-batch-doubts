import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

//Naive approach
class Main {
	public static void main (String[] args) {
		int count = 0;
		Scanner sc =new Scanner(System.in);
		long a =sc.nextLong();
		for (long i = 1; i<= a/2; i++){
			if (a % i == 0){
				count = count + 1;
			}
		}
		System.out.println(count + 1);
	}
}
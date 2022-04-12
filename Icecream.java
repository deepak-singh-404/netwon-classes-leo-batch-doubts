public class Icecream {
    public static int eval(int total_input_icream, int days_count) {

        if (days_count == 0) {
            return total_input_icream;
        }
        int icecream_left = total_input_icream;

        while (days_count > 0) {
            int quotient = icecream_left / 2;
            int multiplier = (icecream_left - quotient) * 3;
            icecream_left = multiplier;
            days_count = days_count - 1;
        }
        return icecream_left;
    }

    public static void main(String[] args) {
        int res = eval(5, 1);
        System.out.println(res);
    }
}
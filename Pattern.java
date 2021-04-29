/**
 * Pattern
 */
public class Pattern {

    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {

            for (int j = 5; j > i; j--) {
                System.out.print("*");
            }
            for (int k = 0; k < 2 * i; k++) {
                System.out.print(" ");
            }
            for (int j = 5; j > i; j--) {
                System.out.print("*");
            }

            System.out.println();
        }
        for (int i = 0; i < 5; i++) {

            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            for (int k = 2 * 5; k > 2 * i + 2; k--) {
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
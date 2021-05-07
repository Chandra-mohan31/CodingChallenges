public class Pattern4 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            for (int k = 5; k > i; k--) {
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int m = 5; m > 0; m--) {
            // for (int s = 0; s < 5; s++) {
            // System.out.print(" ");
            // }
            for (int j = 0; j <= m; j++) {
                System.out.print(" ");
            }
            for (int t = 0; t < m; t++) {
                System.out.print(" *");
            }
            System.out.println();
        }
        for (int i = 0; i <= 5 - 1; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k <= 5 - 1 - i; k++) {
                System.out.print("*" + " ");
            }
            System.out.println();
        }
    }
}

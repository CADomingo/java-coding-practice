package Strings;

public class ReverseString {

    public static void main(String[] args) {

        // Reverse the String / Check Palindrome
        // without using predefined reverse methods

        String s = "Rahul";
        String t = "";

        for (int i = s.length() - 1; i >= 0; i--) {
            t = t + s.charAt(i);
        }

        if (s.equals(t)) {
            System.out.println(t + " is a Palindrome");
        } else {
            System.out.println(t + " is not a Palindrome");
        }
    }
}
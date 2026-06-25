// import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {

       if (s.length() != t.length())
            return false;

       char[] h1=s.toCharArray();
       char[] h2=t.toCharArray();

       Arrays.sort(h1);
       Arrays.sort(h2);

        return Arrays.equals(h1, h2);
       

    }
}

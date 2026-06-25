class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String,List<String>> res =new HashMap<>();

        for (String s: strs){
            char[] chararr=s.toCharArray();
            Arrays.sort(chararr);
            String sorted=new String(chararr);
            res.putIfAbsent(sorted,new ArrayList<>());
            res.get(sorted).add(s);
        }
        return new ArrayList<>(res.values());
        


    }
}

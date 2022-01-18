import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int[] result = new int[id_list.length];
        for (int i=0; i<result.length; i++) {
            result[i] = 0;
            answer[i] = 0;
        }
        HashSet<String> hashSet = new HashSet<>(Arrays.asList(report));
        String[] resultReport = hashSet.toArray(new String[0]);
        for (String s: resultReport) {
            String[] splitReport = s.split("\\s+");
            result[Arrays.asList(id_list).indexOf(splitReport[1])] += 1;
        };
        for (int i=0; i<result.length; i++) {
            if (result[i] >= k) {
                for (String s: resultReport) {
                    String[] splitReport = s.split("\\s+");
                    if(id_list[i].equals(splitReport[1])) {
                        answer[Arrays.asList(id_list).indexOf(splitReport[0])] += 1; 
                    }
                }
            }
        }
        return answer;
    }
}
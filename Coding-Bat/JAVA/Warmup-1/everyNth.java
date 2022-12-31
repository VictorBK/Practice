public String everyNth(String str, int n) {
    String answer = "";
    for (int i = 0; i < str.length(); i = i + n){
        answer = answer + str.charAt(i);
    }
    return answer;
}

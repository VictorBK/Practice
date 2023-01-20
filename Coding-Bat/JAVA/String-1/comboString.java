public String comboString(String a, String b) {
    if(b.length() < a.length()) {
        String tmp = a;
        a = b;
        b = tmp;
    }
    
    return a + b + a;
}
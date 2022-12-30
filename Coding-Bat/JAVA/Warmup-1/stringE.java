public boolean stringE(String str) {
    int num = 0;
    for(int i = 0; i < str.length(); i++) {
        if(str.charAt(i) == 'e')
            num++;
    }
    return 1 <= num && num <= 3;
}
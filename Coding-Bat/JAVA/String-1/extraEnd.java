public String extraEnd(String str) {
    int len = str.length();
    String temp = str.substring(len - 2, len);
    return (temp + temp + temp);    
}

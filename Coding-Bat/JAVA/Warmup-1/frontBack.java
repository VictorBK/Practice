public String frontBack(String str) {
  int n = str.length();
  if(n >= 2){
    return str.substring(n - 1) + str.substring(1, n - 1) + str.substring(0, 1);
    }
    else
    return str;
}

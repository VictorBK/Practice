public String startOz(String str) {
  String start = "";
  if(1 <= str.length() && str.charAt(0) == 'o'){
    start += 'o';
  }
  if(2 <= str.length() && str.charAt(1) == 'z'){ 
    start += 'z';
  }
  return start;
}

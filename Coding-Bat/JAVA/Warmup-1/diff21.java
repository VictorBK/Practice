public int diff21(int n) {
  if(n <= 21){
    return 21 - n;
  }
  
  else if(n > 21){
    return ((n - 21) * 2);
  }
  return 0;
}

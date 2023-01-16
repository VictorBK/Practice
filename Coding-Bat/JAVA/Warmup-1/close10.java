public int close10(int a, int b) {
  int distA = Math.abs(a - 10);
  int distB = Math.abs(b - 10);
      
  if(distA == distB)
    return 0;
                
  return distA < distB ? a : b;
}

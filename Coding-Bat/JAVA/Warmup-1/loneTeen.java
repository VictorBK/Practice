public boolean loneTeen(int a, int b) {
  boolean aTeen = 13 <= a && a <= 19;
  boolean bTeen = 13 <= b && b <= 19;
      
  return aTeen != bTeen;
}

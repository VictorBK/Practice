public String frontTimes(String str, int n) {
  int len = str.length();
    String res = "";
    if (len < 4)
    {
      for (int a = 0; a < n; a++)
      {
    res += str;
      }
    }
    else
    {
      for (int b = 0; b < n; b++) 
      {
        res += str.substring(0, 3);
      }
  }
  return res;
}


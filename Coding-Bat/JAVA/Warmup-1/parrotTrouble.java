public boolean parrotTrouble(boolean talking, int hour) {
  if (!talking)
    return false;
  else if (hour > 20 || hour < 7)
    return true;
  else
    return false;
}

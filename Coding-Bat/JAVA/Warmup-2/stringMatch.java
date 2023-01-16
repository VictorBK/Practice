public int stringMatch(String a, String b) {
    int len = a.length() <= b.length() ? a.length() : b.length();
    len--;
    int count = 0;
    for(int i = 0; i < len; i++)
    {
        if(a.substring(i, i + 2).equals(b.substring(i, i + 2)))
                count++;
    }
    return count;
}

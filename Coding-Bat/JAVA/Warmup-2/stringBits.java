public String stringBits(String str) {
    int size = (int) Math.ceil((double) str.length() / 2);
    char[] result = new char[size];

    int index = 0;
    for(int i = 0; i < str.length(); i += 2) {
        result[index] = str.charAt(i);
        index++;
    }
    return new String(result);
}

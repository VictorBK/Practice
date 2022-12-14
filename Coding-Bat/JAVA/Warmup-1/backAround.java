public String backAround(String str) {
    char last = str.charAt(str.length() - 1);
    return last + str + last;
}

public boolean hasBad(String str) {
    if(str.length() == 3)
        return str.substring(0, 3).equals("bad");

    if(str.length() >= 4)
        return str.substring(0, 3).equals("bad") ||
            str.substring(1, 4).equals("bad");

    return false;    
}
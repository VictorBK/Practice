public String stringX(String str) {
    int len = str.length();
    if(len >= 2) {
        len--;
        StringBuilder stbuild = new StringBuilder(len - 1);
        stbuild.append(str.charAt(0));
        for(int i = 1; i < len; i++) {
            if(str.charAt(i) != 'x')
                stbuild.append(str.charAt(i));
        }
        stbuild.append(str.charAt(len));
        return stbuild.toString();
    }
    else
        return str;    
}

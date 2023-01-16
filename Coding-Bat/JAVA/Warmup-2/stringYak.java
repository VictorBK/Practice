public String stringYak(String str)
{
	int len = str.length();
	int i = 0;
	char ch;
	StringBuilder stbuild = new StringBuilder(len);
	while(i < len)
	{
		ch = str.charAt(i);
		if(i + 2 < len && ch == 'y' && str.charAt(i + 2) == 'k')
			i += 3;
		else
		{
			stbuild.append(ch);
			i++;
		}
	}
	return stbuild.toString();
}

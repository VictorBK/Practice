public String altPairs(String str)
{
	int len = str.length();
	if(len >= 3)
	{
		StringBuilder stbuild = new StringBuilder();
		for(int i = 0; i < len; i += 4)
		{
			stbuild.append(str.charAt(i));
			if(i + 1 < len)
				stbuild.append(str.charAt(i + 1));
		}
		return stbuild.toString();
	}
	else
		return str;
}

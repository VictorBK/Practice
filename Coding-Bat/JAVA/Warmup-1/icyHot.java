public boolean icyHot(int temp1, int temp2) {
    return (temp1 * temp2 < 0) && Math.abs(temp1 - temp2) >= 102;
}


class Solution {
  public int getSum(int a, int b) {
    int car;
    while(b!=0){
      car=a&b;
      a=a^b;
      b=car<<1;
    }
    return a;
  }
}

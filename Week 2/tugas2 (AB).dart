String AngkaBiner(int n) {
  if (n == 0) {
    return "0";
  }

String BinerString = "";
while (n > 0) {
  int sisa = n % 2;
  BinerString = sisa.toString() + BinerString;
  n = n~/ 2;
}
  return BinerString;
}
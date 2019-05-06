def vatCal(price,vat):
    total = price + (price*vat/100);
    return total;
print(vatCal(int(input()),7));
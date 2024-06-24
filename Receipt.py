productlist =[]
pricelist=[]
qtylist=[]
totallist=[]

staffname= input("Enter your staff name: ")
staffID= input("Enter your staff ID: ")

print(f"Welcome {staffID}_{staffname}")

while True:
    productInput = input("Product name: ")
    priceInput = float(input("Product price: "))
    qtyInput = int(input("Product quantity: "))

    productlist.append(productInput)
    pricelist.append(priceInput)
    qtylist.append(qtyInput)
    totallist.append( priceInput * qtyInput )

    cmd = input("Enter another list? [y/n]: ")
    if (cmd == "n"):
        break

overallprice = sum(totallist)
eachprice = (totallist)
listamount = len(productlist)
average = overallprice / sum(qtylist)
maxValue = max(pricelist)
minValue = min(pricelist)

indexMin = pricelist.index(minValue)
indexMax = pricelist.index(maxValue)
nameMin = productlist[indexMin]
nameMax = productlist[indexMax]

print(f"The overall price is: {overallprice}")
print(f"The price for each products are: {totallist}")
print(f"The amounts of lists made are: {listamount}")
print(f"The average price is: {average}")
print(f"The most expesive price is: {maxValue}_{nameMax}")
print(f"The most cheapest price is: {minValue}_{nameMin}")

#Part A = making lists =[], staff name and Id, printing with the f function.

#Part B = while true, the inputs (normal, float and int), list.append(Input),
# totallist.append( priceInput * qtyInput), the cmd and break.

#Part C =
#overallcost = sum(totallist)
#eachcost = (totallist)
#listamount = len(productlist)
#average = overallcost / sum(qtylist)
#maxValue = max(pricelist)
#minValue = min(pricelist)
#indexMin = pricelist.index(minValue)- do for max too
#nameMin = productlist[indexMin]- do for max too
#print with f function.

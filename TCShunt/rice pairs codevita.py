''' question: 
String From Rank
In a Super market we will find many variations of the same product. In the same way we can find many types of rice bags which differ in its quantity, price, brand, and type of rice in it. Many variations of same products exist in a super market. Consider rice for example. We get it in varying quantities 
(
q
)
(q) and at different prices 
(
p
)
(p).
Thus rice bag is unique combination of 
q
,
p
q,p. Customers want to buy the rice bags of their own choices. Each bag has two attributes price and the quantity of rice. The customers have some conditions for buying the rice bags, they have a specific price and quantity that have to be compared with the rice bags before buying them. If the price of rice bag is less than or equal to the customer’s preference and if the quantity is more than given preference, then he/she will buy it. There is only one bag of each type and each customer can buy at most one bag.
Given 
n
n,
m
m representing the number of customers and rice bags respectively, along with the variations of rice bags available in the market and the preferences of customers, find the maximum number of bags that can be sold by the end of the day.

Input Format The first line contains two space separated integers n n
and m m denoting the number of customers and number of rice bags
respectively. Next n n lines consist of two space separated integers a a
and b b denoting customer’s preferences viz. customer’s quantity and
cost preferences, respectively. Lastly, the next m m lines consist of
two space separated integers q and p denoting the bags quantity and
cost, respectively. Output Format Print the maximum number of rice bags
that can be sold input 5 4 35 2400 70 5500 87 6000 20 1700 12 500 50
2500 75 4875 100 7000 25 1250 output 2

'''



# Read the number of customers (n) and the number of rice bags (m)
n, m = map(int, input().split())

# Initialize a list to store customers' preferences
cust = []
for _ in range(n):
    q, p = map(int, input().split())  # Read quantity (q) and price (p) for each customer
    cust.append([p, q])  # Store preferences as [price, quantity]

# Initialize a list to store rice bag details
rice = []
for _ in range(m):
    q, p = map(int, input().split())  # Read quantity (q) and price (p) for each rice bag
    rice.append([p, q])  # Store details as [price, quantity]


# Sort the customers by their price preference
cust.sort()

# Sort the rice bags by their price
rice.sort()

# Initialize a list to track which rice bags have been used
count = [0] * m

# Initialize a variable to count the number of satisfied customers
ans = 0

# Process each customer
for i in range(n):
    quan = -1  # To track the quantity of rice that can be selected for the current customer
    index = -1  # To track the index of the selected rice bag
    for j in range(m):
        if not count[j]:  # Check if the rice bag has not been used
            if rice[j][0] > cust[i][0]:  # If the rice bag's price exceeds the customer's budget
                break  # No more suitable rice bags can be found
            # Check if the rice bag's quantity can satisfy the customer's quantity preference
            if rice[j][1] > cust[i][1]:
                # If this is the first valid rice bag or it has a smaller quantity
                if quan == -1:
                    quan = rice[j][1]  # Set the quantity to the current rice bag's quantity
                    index = j  # Save the index of the current rice bag
                else:
                    if quan > rice[j][1]:  # If a better option is found
                        index = j  # Update the index
                        quan = rice[j][1]  # Update the quantity

    # If a suitable rice bag is found, mark it as used
    if index != -1:
        count[index] = 1  # Mark the rice bag as used
        ans += 1  # Increment the count of satisfied customers

# Output the total number of satisfied customers
print(ans)



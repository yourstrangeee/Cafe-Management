def main():
    menus = {
        "pizza": 40,
        "pasta": 50,
        "burger": 60,
        "salad": 70,
        "coffee": 80
    }
    
    print("Welcome To Our Coffee Shop")
    print("pizza : 40rs\npasta : 50\nburger : 60\nsalad : 70\ncoffee : 80")
    
    while True:
        price = 0
        order_items = []
        
        while True:
            order = input("Enter The Dish You Want (or type 'done' to finish ordering): ")
            
            if order == "done":
                break
            
            if order in menus:
                price += menus[order]
                order_items.append(order)
                print(f"Your Order {order} Successfully Ordered. Total Bill so far: {price}")
            else:
                print(f"{order} is not in menus. Please choose from the menu.")
        
        print(f"You have ordered {len(order_items)} item(s) in total.")
        print(f"Your Total Bill: {price}")
        
        order2 = input("Do You want something else? (Y/N): ")
        if order2.upper() != "Y":
            break

main()
# cafe management by your strange dm [yxrs_strange] if you want to upgrade or want to suggest some ideas 

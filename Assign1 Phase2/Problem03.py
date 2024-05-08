list=["Palak Paneer","Dhokla","Paav Bhaaji"]
def get_order(list):
    stack=[]
    for order in list:
        print(f"Preparing Your Order - ({order})")
        stack.append(order)
    print("\nThe following orders have been dispatched: ")
    while stack:
        dispatched_order=stack.pop(0)
        print(dispatched_order)
        
get_order(list)

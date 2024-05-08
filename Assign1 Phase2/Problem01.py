def get_name():
    name=input("Enter your name: ")
    return name

def get_tshirt(brand_name):
    user_name=get_name()
    list=["Nike","Adidas","Levi's","Fila","Puma"]
    if brand_name in list:
        print(f"Hi {user_name}, the brand you are looking for is available in our store")
    else:
        print(f"Hi {user_name}, Unfortunately the brand you are looking for is not available in our store")

get_tshirt("Nike")

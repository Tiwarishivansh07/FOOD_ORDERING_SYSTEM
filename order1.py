# Column Alignment: Used :< format specifiers to align the text under headers

def food_ordering_system():
    print("---------------------------------------------------------------------")
    print("Welcome to our food ordering app. We will give you the best price!") 
    print("---------------------------------------------------------------------")

    Veg_menu = ["Paneer", "Rice", "Chapati"]
    zomato_Price_veg_menu = [300, 250, 50]
    swiggy_Price_veg_menu = [200, 300, 60]

    non_veg_menu = ["Chicken", "Mutton", "Chicken Biryani"]
    zomato_price_non_veg_menu = [450, 350, 280]
    swiggy_price_non_veg_menu = [100, 400, 240]

    GST_RATE = 0.05  # 5% GST
    SERVICE_TAX = 0.1  # 10% Service Tax

    selected_dish = []
    selected_dish_price = []

    while True:
        print("\nSelect an option:")
        print("1. Veg Menu")
        print("2. Non-Veg Menu")
        print("3. To print the bill ")
        print("4. Exit")

        select = input("Enter the option you want to select (1/2/3/4): ")

        if select == "1":
            print("\n------------------ The Veg Menu ----------------------")
            print(f'{"Dish":<20} {"Zomato Price":<15} {"Swiggy Price":<15}')
            print("-" * 50)
            for dish, zomato_price, swiggy_price in zip(
                Veg_menu, zomato_Price_veg_menu, swiggy_Price_veg_menu
            ):
                print(f"{dish:<20} ₹{zomato_price:<14} ₹{swiggy_price:<14}")

            dish_select = input("\nEnter the dish you want to eat: ")
            if dish_select in Veg_menu:
                i = Veg_menu.index(dish_select)
                print(f"\nThe dish you have selected is {Veg_menu[i]}")
                print(
                    f"The price of that dish on Zomato is ₹{zomato_Price_veg_menu[i]}"
                )
                print(
                    f"The price of that dish on Swiggy is ₹{swiggy_Price_veg_menu[i]}"
                )
                platform = input("\nChoose the platform (Zomato/Swiggy): ").lower()
                if platform == "zomato":
                    selected_dish_price.append(zomato_Price_veg_menu[i])
                elif platform == "swiggy":
                    selected_dish_price.append(swiggy_Price_veg_menu[i])
                else:
                    print("Invalid input. Please select Zomato or Swiggy.")
                    continue
                selected_dish.append(Veg_menu[i])
            else:
                print("\nInvalid dish selected. Please choose a dish from the menu.")

        elif select == "2":
            print("\n------------------ The Non-Veg Menu ------------------")
            print(f'{"Dish":<20} {"Zomato Price":<15} {"Swiggy Price":<15}')
            print("-" * 50)
            for dish, zomato_price, swiggy_price in zip(
                non_veg_menu, zomato_price_non_veg_menu, swiggy_price_non_veg_menu
            ):
                print(f"{dish:<20} ₹{zomato_price:<14} ₹{swiggy_price:<14}")

            dish_select = input("\nEnter the dish you want to eat: ")
            if dish_select in non_veg_menu:
                i = non_veg_menu.index(dish_select)
                print(f"\nThe dish you have selected is {non_veg_menu[i]}")
                print(
                    f"The price of that dish on Zomato is ₹{zomato_price_non_veg_menu[i]}"
                )
                print(
                    f"The price of that dish on Swiggy is ₹{swiggy_price_non_veg_menu[i]}"
                )
                platform = input("\nChoose the platform (Zomato/Swiggy): ").lower()
                if platform == "zomato":
                    selected_dish_price.append(zomato_price_non_veg_menu[i])
                elif platform == "swiggy":
                    selected_dish_price.append(swiggy_price_non_veg_menu[i])
                else:
                    print("Invalid input. Please select Zomato or Swiggy.")
                    continue
                selected_dish.append(non_veg_menu[i])
            else:
                print("\nInvalid dish selected. Please choose a dish from the menu.")

        elif select == "3":
            payment_select=input("Enter the method of payment Cod / online").lower()

            if payment_select=='cod':
                name=input("Enter the Name ")
                address=input("Enter the address")
                phone_no=int(input("Enter the phone number"))
                '\n'
            # Calculate total bill
                total_without_tax = sum(selected_dish_price)
                gst = total_without_tax * GST_RATE
                service_tax = total_without_tax * SERVICE_TAX
                total_with_tax = total_without_tax + gst + service_tax

                print("\n------------ BILL -------------")
                print(f"The Name of Customer is :{name}")
                print(f'The delivery address is :{address}')
                print(f'The phone number is :{phone_no}')
                '\n'
                print(f'{"Dish":<20} {"Price":<15}')
                for dish, price in zip(selected_dish, selected_dish_price):
                    print(f"{dish:<20} ₹{price:<14}")
                print("-" * 35)
                print(f"{'Total (without tax)':<20} ₹{total_without_tax:<14}")
                print(f"{'GST (5%)':<20} ₹{gst:<14}")
                print(f"{'Service Tax (10%)':<20} ₹{service_tax:<14}")
                print(f"{'Total (with tax)':<20} ₹{total_with_tax:<14}")
                print("-" * 35)
            
            elif payment_select=='online':
                name=input("Enter the Name ")
                phone_no=int(input("Enter the phone number"))
            # Calculate total bill
                total_without_tax = sum(selected_dish_price)
                gst = total_without_tax * GST_RATE
                service_tax = total_without_tax * SERVICE_TAX
                total_with_tax = total_without_tax + gst + service_tax

                print("\n------------ BILL -------------")
                print(f"The Name of Customer is :{name}")
                print(f'The phone number is :{phone_no}')
                print(f'{"Dish":<20} {"Price":<15}')
                for dish, price in zip(selected_dish, selected_dish_price):
                    print(f"{dish:<20} ₹{price:<14}")
                print("-" * 35)
                print(f"{'Total (without tax)':<20} ₹{total_without_tax:<14}")
                print(f"{'GST (5%)':<20} ₹{gst:<14}")
                print(f"{'Service Tax (10%)':<20} ₹{service_tax:<14}")
                print(f"{'Total (with tax)':<20} ₹{total_with_tax:<14}")
                print("-" * 35)

        elif select == "4":
            print("Thank you for using the food ordering app. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")
food_ordering_system() 


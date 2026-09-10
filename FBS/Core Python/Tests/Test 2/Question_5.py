for i in range (1,6):
    price = float(input('Enter the price of product:'))
    total_price += price

    gst_amount = total_price*0.18

    total_bill = total_price + gst_amount
    print(f'total_bill_after_adding_18%_GST:{total_bill})
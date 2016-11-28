#Created by: Hamza Salman
#Created for: ICS3U
#Created on: November 2016
#This is a cash register program for assignment 7.

import ui

HST = 0.13
subtotal = 0
tax = 0
total = 0
counter = 0
items = []


def add_item_button_touch_up_inside(sender):
    #This function adds items to the items array
    
    if len(items) > 10:
        view['error_label'].text = 'sorry we can only have 10 items per recipt.'
    elif float(view['cost_input_textfield'].text) <= 0:
        view['error_label'].text = 'please enter an integer value greater than zero for the cost.'
    else:
        items.append(float(view['cost_input_textfield'].text))
        view['number_of_items_label'].text = str(len(items))
        view['cost_input_textfield'].text = ''
        
def print_recipt_button_touch_up_inside(sender):
    #This function uses the information in the array to solve for subtotal, tax and total and outputs them onto a recipt
    
    global subtotal
    global tax
    global total
    global counter
    
    subtotal = 0
    tax = 0
    total = 0
    counter = 0
    
    if len(items) == 0:
        view['error_label'].text = 'Add some items first!'
    else:
        view['number_of_items_recipt_label'].text = 'number of items: ' + str(len(items))
        view['items_list_label'].text = ''
        for item in items:
            subtotal = subtotal + item
            counter = counter + 1
            view['items_list_label'].text = view['items_list_label'].text + '\n' + 'item #' +str(counter) +  ' -> ' + str(item)
            
    tax = float(subtotal) * float(HST)
    total = float(subtotal) + float(tax)
    
    view['subtotal_label'].text = 'The subtotal is: ' + '${:,.2f}'.format(subtotal);
    view['HST_label'].text = 'The HST is: ' + '${:,.2f}'.format(tax);
    view['total_label'].text = 'The total is: ' + '${:,.2f}'.format(total);
    
def new_transaction_touch_up_inside(sender):
    #This function resets all the information so the program can be used again without manually turning it off and on again.
	
    global subtotal
    global tax
    global total
    global counter
    
    subtotal = 0
    tax = 0
    total = 0
    counter = 0
    
    view['number_of_items_label'].text = ''
    view['number_of_items_recipt_label'].text = ''
    view['items_list_label'].text = ''
    view['subtotal_label'].text = ''
    view['HST_label'].text = ''
    view['total_label'].text = ''
    view['error_label'].text = ''
    view['cost_input_textfield'].text = ''
    while len(items) > 0:
        for everything in items:
            items.remove(everything)
    
view = ui.load_view()
view.present('fullscreen')

product1_name, product1_price = input("Product1 Name : "), input("Product1 price : ")
        product2_name, product2_price = input("Product2 Name : "), input("Product2 price : ")
        product3_name, product3_price = input("Product3 Name : "), input("Product3 price : ")
        company_name = input("Enter your Company name : ")
        company_address = input("Enter your Company Address : ")
        company_city = input("Enter your Company City : ")
        # declare ending message
        message = 'Thanks for shopping with us today!'
        # create a top border
        print('*' * 50)
        # print company information first using format
        print('\t\t{}'.format(company_name.title()))
        print('\t\t{}'.format(company_address.title()))
        print('\t\t{}'.format(company_city.title()))
        # print a line between sections
        print('=' * 50)
        # print out header for section of items
        print('\tProduct Name\tProduct Price')
        # create a print statement for each item
        print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
        print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
        print('\t{}\t\t${}'.format(product3_name.title(), product3_price))
        # print a line between sections
        print('=' * 50)
        # print out header for section of total
        print('\t\t\tTotal')
        # calculate total price and print out
        total = sum(product1_price + product2_price + product3_price)
        print('\t\t\t${}'.format(total))
        # print a line between sections
        print('=' * 50)
        # output thank you message
        print('\n\t{}\n'.format(message))
        # create a bottom border
        print('*' * 50)

# Importing cash_on_hand, overheads and profit_loss files into this file
import cash_on_hand, overheads, profit_loss


def main():
    """
    Function that executes all 3 functions in previously imported files
    """
    
    # Executes the overhead() function from the overheads file
    overheads.overhead()
    
    # Executes the value() function from the cash_on_hand file
    cash_on_hand.value()
 
    # Executes the profit() function from the profit_loss file
    profit_loss.profit()

# Executes the main function
main()

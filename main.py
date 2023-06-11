import data_analysis.cleaning as cl 
import pandas as pd
import numpy as np
from sql1.database_actions import create_tables_from_df 
import functions


def main():
    #This is the main menu of the program
    # In main(), read in the csv and call the cleaning functions from your cleaning file.
    # hotel_bookings = pd.read_csv("C:/Users/Simcha/Down2loads/HotelReservationsnew/HotelReservations/hotel_bookings.csv").replace(['([uU]ndefined)', '/^(\S) &', '/^([nN]one)$', '/^(-)$'], np.nan, regex=True)
    # cl.clean_df(hotel_bookings)
    
    # create_tables_from_df(hotel_bookings)
    functions.menu()



    
if __name__ == "__main__":
    main()
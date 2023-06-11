from sql1 import queries
from entities import Reservation
import logging
import logs

logging.basicConfig(filename= "C:/Users/Simcha/Documents/Integralytic/Hotel Reservations Midterm Project/hotel_reservations/logs/hotel_logs.txt",
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)



countries = ['ISR', 'BOL', 'CHN', 'TGO', 'SYR', 'CHL', 'SLE', 'COL', 'AND', 'JPN', 'GUY', 'IRQ', 'SYC', 'NZL', 'PLW',\
             'UZB', 'USA', 'ARG', 'KNA', 'PRT', 'AUS', 'MEX', 'SVN', 'GIB', 'ATA', 'ARE', 'HRV', 'DEU', 'VEN', 'NLD',\
             'HKG', 'SVK', 'CHE', 'PRI', 'KAZ', 'LBN', 'MYS','IDN', 'BDI', 'CZE', 'NAM', 'ARM', 'NIC', 'GAB', 'ITA', \
             'URY', 'KOR', 'ZWE', 'DJI','SAU', 'CRI', 'VNM', 'STP', 'PYF', 'TUR', 'MRT', 'DMA', 'ALB', 'LCA', 'FRO', \
             'BEN', 'MLI', 'IRL', 'POL', 'NGA', 'MKD', 'AUT', 'JEY', 'CUB', 'IMN', 'TZA', 'KEN', 'BEL', 'BRA', 'BFA', \
             'MAC', 'FIN', 'MMR', 'FJI', 'GEO', 'MAR', 'GGY', 'CYM', 'GHA', 'MYT', 'LTU', 'EGY', 'MDV', 'MNE', 'PAK', \
             'ATF', 'DNK', 'ZAF', 'CIV', 'DZA', 'BGR', 'RWA', 'MDG', 'BHR', 'SGP', 'RUS', 'PRY', 'GRC', 'ROU', 'OMN', \
             'HND', 'AIA', 'LUX', 'THA', 'JOR', 'CAF', 'LIE', 'BWA', 'SRB', 'TUN', 'SWE', 'SEN', 'VGB', 'TWN', 'MLT', \
             'SUR', 'TMP', 'CMR', 'SDN', 'COM', 'MWI', 'BLR', 'EST', 'UGA', 'SMR', 'KWT', 'FRA', 'DOM', 'PAN', 'NCL', \
             'IRN', 'GLP', 'IND', 'PHL', 'MOZ', 'ISL', 'SLV', 'ESP', 'LVA', 'GBR', 'AZE', 'CYP', 'GNB', 'LKA', 'UMI', \
             'ABW', 'ECU', 'LAO', 'PER', 'ETH', 'QAT', 'MCO', 'KHM', 'AGO', 'CPV', 'HUN', 'GTM', 'BIH', 'UKR', 'JAM', \
            'KIR', 'NPL', 'LBY', 'BRB', 'TJK', 'NOR', 'CN', 'MUS', 'BHS', 'BGD', 'ZMB', 'ASM']
def pick_country():
    #This is to get user input on which country to run the query on top agents reservations per country and then runs the query
    country = input("Which country?\n")
    if country in countries:
        result = queries.get_top_agents_reservations_in_country(country)
        list = []
        for index, row in result.iterrows():
            r = Reservation.Reservation.__str__(row)
            list.append(r)
        for i in list:
            print(i)
        logging.info("ran successfully")    

    else:
        print('That is not valid. Please pick from the list: \n' + ', '.join(countries))
        pick_country()
        logging.info("invalid country chosen") 

def pick_year_ADR1_ADR2():
    #This gets user input on yr, adr min and adr max then uses input to run adn return query of get info for yr within adr
    year = int(input("Pick a year between 2014 and 2017\n"))
    ADR1 = int(input("Pick min adr value between range of -6 and 5400\n"))
    ADR2 = int(input("Pick max adr value between range of -6 and 5400\n"))
    if (2014 <= year <= 2017) and (-6 <= ADR1 <=  5400) and (-6 <= ADR2 <= 5400):
        result = queries.get_info_for_yr_within_adr(year, ADR1, ADR2)
        list = []
        for index, row in result.iterrows():
            r = Reservation.Reservation.__str__(row)
            list.append(r)
    
        for i in list:
            print(i)
            
    else:
        print("Please ensure valid input:")
        pick_year_ADR1_ADR2()
        logging.info("invalid yr, adr1, or adr2 chosen") 

def menu():
    #This executes the menu for the hotel manager
    userInput = input("Would you like 1. get_top_agents_reservations_in_country 2. get_info_for_yr_within_adr" \
                        " 3. show_num_children_impacts_nights  4.average_adr_per_country\n" )
    if userInput == "1":
        pick_country()
    elif userInput == "2": 
        pick_year_ADR1_ADR2()
    elif userInput == "3": 
        result = queries.show_num_children_impacts_nights()
        
        print(result)
            
    elif userInput == "4": 
        result = queries.average_adr_per_country()
        
        print(result)
            
    else:
        print ("That is an invalid entry.  Please type a number 1-4\n")
        menu()  
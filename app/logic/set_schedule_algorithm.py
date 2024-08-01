    """
    Questions to ask:
    
    1. What format should the data be organized in?
        - User should be able to input all the necessary data via a text file. The txt file should be parsed into
          a usable python dict, that can be processed by the algo.
        - Initial testing data is gathered via webscraper on the wellness living app

    2. How much of the contraints/data does the user get to control?
        The user simply specifies the preferred amount of max sessions in each location, and a list of clients and preferred times for each client.
        The schedule should not make it so that the amount of people in either location exceed their capacity.
        For example: 
        define location 1 capactiy
        define location 2 capacity
        define possible overlap (15 mins 5 people at location 1)
        
    3. Where does the data come from?
        txt file that is parsed by the script, and uploaded by the user manually (perhaps saved in database after parsing?)

    4. What algorithm do you use?

    5. What will the output look like?
        Output will spit out an actual schedule much like the wellness living, and give the user the option to save a list of times and locations
        in a txt file. 

    6. Do we involve ai?
        no.

    7. How adaptable should this script be? Are contraints maleable?
        Locations can be added, and clients times can be changed to produce new schedules. Old schedules need to be saved.

    Notes: 
    Additional features: The user should be able to input a list of clients with their current schedules and the program should 
                         determine whether it meets the constraints of the preffered schedule or not.
    """
     
def set_schedule():


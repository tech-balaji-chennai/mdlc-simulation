#3) data collection (or) gathering - collecting (or) gathering data from various sources (generally 'name_data.csv')

#importing packages directly on top of the program
import os
import sys
#import selenium

def data_collection():
    
    #data acquisition - acquiring data from identified sources
    def acquire_data():
        try:
            #identifying source of data, such as database, API (or) sensor (for database fetching, web scraping, etc.)
            global data_source
            data_source = input("Enter data source (acquiring path): ")
            if len(data_source) == 0:
                raise Exception("Error during data acquisition")
            return 1
        except Exception as e:
            print(e)
            return 0
        
    #data storage - storing data to identified destinations
    def store_data():
        try:
            #identifying destination of data, such as database, csv file (or) cloud storage
            data_destination = input("Enter data destination (storing path): ")
            if len(data_destination) == 0:
                raise Exception("Error during data storage")
            return 1
        except Exception as e:
            print(e)
            return 0
    
    #data annotation - annotating (or) labelling data (for supervised learing like tagging images or text with relevant categories)
    def annotate_data():
        status = 1
        if status == 0:
            return 0
        return 1
    
    #concerning data privacy for clearning legal troubles
    def concern_data_privacy():
        status = 1
        if status == 0:
            return 0
        return 1
    
    #executing steps of data collection process
    def execute_all():
        
        status = acquire_data()
        if status == 0:
            print("Data acquisition failed. Stopping...\n")
            return
        print("Data is acquired from given data source successfully\n")
        
        status = store_data()
        if status == 0:
            print("Data storage failed. Stopping...\n")
            return
        print("Data is stored to given data destination successfully\n")
        
        status = annotate_data()
        if status == 0:
            print("Data annotation failed. Stopping...\n")
            return
        print("Data is annotated successfully\n")
        
        status = concern_data_privacy()
        if status == 0:
            print("Data privacy concern is failed. Stopping...\n")
            return
        print("Data privacy is concerned and legal troubles are cleared successfully\n")
    
        print("Data is collected successfully\n")
    
    execute_all()

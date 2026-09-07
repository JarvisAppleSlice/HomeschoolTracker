import streamlit as st

# Time formatting

def format_time(time):
    if time < 60:
        time_display = f'{time} min'
    
    else:
        hrs = time // 60
        mins = time % 60

        if mins == 0 and hrs == 1:
            time_display = f'{hrs} hr'
        
        elif mins == 0:
            time_display = f'{hrs} hrs'    
        
        elif hrs > 1:
            time_display = f'{hrs} hrs {mins} mins'
        
        else:
            time_display = f'{hrs} hr {mins} mins'  

    return time_display
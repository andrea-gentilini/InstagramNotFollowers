from datetime import datetime
import matplotlib.pyplot as plt

"""
Please read the README file before running this code
In order to fully understand the purpose and the execution of this code
"""

def clean_line(line):
    cleaned_line = line.strip()
    cleaned_line = cleaned_line[1:]
    if cleaned_line.startswith("value"):
        return cleaned_line[8:-1]
    return None


def load_set_from_file(filename):
    data_set = set()
    with open(filename, 'r') as file:
        for line in file:
            cleaned_line = clean_line(line)
            if cleaned_line is not None:
                data_set.add(cleaned_line)
    return data_set


def days_between_dates(date1, date2):
    # Convert dates to datetime objects
    dt1 = datetime(date1[2], date1[0], date1[1])
    dt2 = datetime(date2[2], date2[0], date2[1])

    # Calculate the difference between the two dates
    delta = dt2 - dt1

    # Extract the number of days from the difference
    days = delta.days

    return days


def str_to_list(date_string):
    # Remove the square brackets and split the string into individual elements
    date_string = date_string.strip('[] ')
    date_elements = date_string.split(',')
    
    # Convert the elements to integers and create the final list
    date_list = [int(element.strip()) for element in date_elements]
    
    return date_list


def update_followers(number_of_followers, username):

    #trick so I don't have to import the OS library - the following 2 lines of code are needed only for the first time running this code
    file = open(f"{username}_followers_variation.txt", 'a')
    file.close()

    # check the date for the current numbs of followers 
    current_datetime = datetime.now()
    curr_date = current_datetime.date()
    year, month, day = curr_date.year, curr_date.month, curr_date.day
    current_date = [month, day, year]
    
    # check how much time has passed since the last followers update
    distance = None
    with open(f"{username}_followers_variation.txt", 'r') as file:
        lines = file.readlines()
        if not lines: distance = 0
        else:
            last_line = lines[-1]
            last_date_unclear = last_line[:13]
            last_date = str_to_list(last_date_unclear)
            distance = days_between_dates(last_date, current_date)

    # update data
    with open(f"{username}_followers_variation.txt", 'a') as f:
        f.write(f"{current_date} , {number_of_followers}, {distance}.\n")
    
    # update file for plotting
    file_for_plotting(distance, number_of_followers, username)

    return 


def file_for_plotting(distance, number_of_followers, username):
    # updates a text file with the aim of creating easily a plot
    with open(f"{username}_data_for_plotting.txt", 'a') as f:
        f.write(f"{distance}\n")
        f.write(f"{number_of_followers}\n")

    return 


def following_but_not_followers(username):
    # returns a set of people that you are following but that they are not following you back
    followings = load_set_from_file(f"{username} - following.json")
    followers = load_set_from_file(f"{username} - followers.json")
    # P.S. sets are faster and usable since we don't expect duplicates

    # collects data for future applications
    update_followers(len(followers), username)

    not_followers = followings - followers

    print(f'n. followers: {len(followers)}')
    print(f'n. following: {len(followings)}')

    return 'not following you back:', len(not_followers), not_followers


def load_plot_followers_variation():
    xs, ys = [], []

    with open(f"{username}_data_for_plotting.txt", 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            xs.append(int(lines[i]))
            ys.append(int(lines[i+1]))
        
    # Check if the lengths of xs and ys match
    if len(xs) != len(ys):
        raise ValueError("Lists xs and ys must have the same length.")

    # Create the plot
    plt.figure()
    plt.plot(xs, ys, marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Number of followers')
    plt.title('Followers variation')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    username = input('Please input the username you want to analyze: ')
    result = following_but_not_followers(username)
    var = input('Do you also want to know the variation of your followers you had in the time? [Y] Yes    [N] No    -> ')
    if var not in {'Y', 'N'}:
        print('Input not valid, please rerun the program.')
    elif var == 'Y':
        result_2 = load_plot_followers_variation()
    else:
        result_2 = None
    
    print(result)
    if result_2: print(result_2)

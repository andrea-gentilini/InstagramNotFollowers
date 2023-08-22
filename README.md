# InstagramNotFollowers - Easily find out who doesn't follow you back on Instagram

--> INTRODUCTION

This tool enables you to easily verify if people follow you on Instagram, providing a simple and highly effective method that is completely legal, utilizing the official data download provided by Instagram. Refer to the conclusions for a comprehensive understanding of this project.

Now, please follow these steps:

1. Download your Instagram followers/following information.
2.  Organize the necessary files in an appropriate directory.
3. Execute the code and check the results.

-------------------------------------------

--> HOW TO

i) DOWNLOAD YOUR INSTAGRAM FOLLOWERS/FOLLOWING INFORMATION:

1. Open the Instagram mobile app on your personal device.

2. From your profile, navigate to "Your activity."

3. Under "Your activity," go to "Download your information," then select "Request a download" and choose your Instagram account.

At this point, you can select various types of data to download. For the purpose of this project, please follow the instructions below.

4. Choose the types of information to download: Select "Followers" and "Following."

5. Proceed to select your personal email address for data notifications, opt for the JSON format, and set the date range to "All time."

After a few minutes, you will receive an email from Meta with the subject: "Your Meta information download is ready." Open the email and download the provided zip file.


ii) ORGANIZE THE FILES YOU NEED IN A PROPER DIRECTORY:

1. Unzip the downloaded zip file named "instagram-{your username}" and locate the "followers_1" and "following" files.
2. Create a new project folder and install the required "datetime" and "matplotlib" libraries in your virtual environment.
3. Move the "followers_1" and "following" files to the new project folder.
4. Rename these files respectively as "{your username} - followers" and "{your username} - following."
5. Download the "main.py" file from this repository and place it in the same project directory.


iii) RUN THE CODE AND ENJOY:

- Run the "main.py" file from the console.
- Input your Instagram username when prompted. This choice enables the analysis of multiple profiles while keeping all the data in the same folder (e.g., if a friend uses this tool on your laptop).
- Overwrite the old "followers_1" and "following" files with the newly downloaded files each time you update your information.
- You will be asked, "Do you also want to know the variation of your followers you had over time?" If you type "Y," you will receive the list of non-following accounts and a plot of your followers' variation over time.
- Even if you reply "N" to the previous question, your followers' count for that day will be stored in a text file (within the same directory) for potential future reference.
- Please note that this tool is manual and private. Your data will only be stored in your memory, and followers' variations will be measured upon downloading new data and running the code.
This should provide a comprehensive understanding of how to use your tool and its features.

-----------------------------------------------------------
--> CONCLUSION

Hopefully, you've found this code to be beneficial. I chose to develop this project because while there are numerous apps available on popular stores that promise similar information, they often come with critical issues such as profile suspension or excessive advertisements. In contrast, this solution offers a straightforward and effective method to achieve the desired results (something I find particularly appealing). Importantly, it carries no risks of Instagram bans or suspensions, as the collected data is both personal and obtained legally.

The code is versatile and can be easily adjusted to gather different types of information. For instance, you could modify it to track 'who unfollowed you since the last update', expanding its utility even further.

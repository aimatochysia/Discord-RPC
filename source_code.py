#This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License] (CC BY-NC-SA)
import os
import random
import win32gui
import sys
import requests
import time
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from pypresence import Presence


def get_unique_window_titles():
    unique_titles = set()
    def winEnumHandler(hwnd, ctx):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowVisible(hwnd) and title:
            unique_titles.add(title)
    win32gui.EnumWindows(winEnumHandler, None)
    unique_titles_list = list(unique_titles)
    return unique_titles_list


def process_array(input_array):
    output_array = []

    for element in input_array:
        # Check for VS code
        if "Visual Studio" in element:
            extension = element.split(".")[-1].split(" ")[0]
            title = element.split(" - ")[0]
            workspace = element.split(" - ")[1]
            if extension == "py":
                output_array.append(["python logo", "Sticker", f"Coding {title} in {workspace} using PYTHON MY BELOVED"])
            elif extension == "c":
                output_array.append(["programming rust c lang cpp cplusplus", "Gif", f"Coding {title} in {workspace} using HolyC"])
            elif extension == "rs":
                output_array.append(["programming rust c lang cpp cplusplus", "Gif", f"Coding {title} in {workspace} using rusted lol"])
            elif extension == "php":
                output_array.append(["php logo", f"Coding {title} in {workspace} using PHP"])
            elif extension == "csharp":
                output_array.append(["c sharp logo", "Sticker", f"Coding {title} in {workspace} using C#"])
            elif extension == "cpp":
                output_array.append(["c++ logo", "Sticker", f"Coding {title} in {workspace} using C++"])
            elif extension == "java":
                output_array.append(["77 astolfo", "Gif", f"Coding {title} in {workspace} using Java (send help)"])
            elif extension == "jsx":
                output_array.append(["77 astolfo", "Gif", f"Coding {title} in {workspace} using ReactJS"])
            elif extension == "js":
                output_array.append(["java script persona 4 chie chie satonaka my beloved", "Gif", f"Coding {title} in {workspace} using Javascript"])
            elif extension == "html":
                output_array.append(["web developers programmers javascript php css react", "Gif", f"Coding {title} in {workspace} using HTML"])
            elif extension == "css":
                output_array.append(["web developers programmers javascript php css react", "Gif", f"Coding {title} in {workspace} using CSS"])
            else:
                output_array.append([f"{extension} name", "Gif", f"Coding {title} in {workspace} using {extension}"])

        # Check for browser
        elif "Google Chrome" in element or "Opera" in element:
            title = element.split(" - ")[0]
            if "twitch" in title:
                output_array.append(["nyanner", "Gif", "watching Twitch.TV"])
            elif "youtube" in title:
                output_array.append(["rin penrose idol en e sekai vtuber", "Gif", "Watching Youtube"])
            elif "chatgpt" in title:
                output_array.append(["monika", "Sticker", "Fixing codes. . ."])
            elif "docs" in title:
                output_array.append(["tsnsaec nsa bang hack secret", "Gif", f"Editing {title} Docs"])
            elif "/ X" in title:
                output_array.append(["victory macho man laughing emoji good morning monday pumped meme doge elon musk", "Gif", "Canceling Someone on Twitter"])
            else:
                output_array.append(["nicole class of 09 picmix", "Gif", "Browsing Google. . ."])
        
        
        #Social Medias
        elif "Discord" in element:
            output_array.append(["discord", "Gif", "Obviously online in discord"])
        
        elif "LINE" in element:
            output_array.append(["line messenger", "Meme", "Online in LINE"])
        
        elif "Whatsapp" in element:
            output_array.append(["whatsapp", "Gif", "Online in Whatsapp"])
            
        elif "Telegram" in element:
            output_array.append(["telegram", "Gif", "Online in Telegram"])
            
        else:
            words = element.split(" ")
            if len(words) >= 3:
                output_array.append([" ".join(words[:2]), "Gif", "".join(words[:2])])
            else:
                output_array.append([element, "Gif", "".join(words[:2])])
    return output_array


def get_first_gif_src(input_list):
    output_list = []
    for entry in input_list:
        search_query = entry[0]
        class_name = entry[1]
        additional_info = entry[2]
        url = f'https://tenor.com/search/{search_query.replace(" ", "-")}-gifs'
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            gif_div = soup.find('div', class_=class_name)
            if gif_div:
                img_element = gif_div.find('img')
                if img_element:
                    src_attribute = img_element.get('src')
                    output_list.append([src_attribute, additional_info])
                else:
                    print(f"No img element found in the div with class '{class_name}'")
            else:
                print(f"No div with class '{class_name}' found")
        else:
            print(f"Failed to retrieve the page for query '{search_query}'. Status code: {response.status_code}")
    return output_list


def update_rpc(data_list):
    list_length = len(data_list)
    counter = 0
    while (counter < list_length*5):
        temp = data_list[counter % list_length]
        var_link, var_text = temp
        #temp_large_text,temp_state
        RPC.update(
            large_image=var_link,
            large_text="Provided by Tenor.com",
            details=var_text,
            state="RPC by Petra Michael",
            start="1",
            buttons=[{"label": "Github Repository", "url": "https://github.com/aimatochysia/Discord-RPC"}]
        )
        print("-------------------------")
        print(var_text)
        counter+=1
        time.sleep(3)



file_path = "saved_client_id.md"
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        existing_client_id = file.read().strip()
    if existing_client_id:
        print(f"Found existing client ID: {existing_client_id}")
        use_existing = input("Do you want to use the existing client ID? (y/n): ").lower()
        if use_existing == 'y':
            client_id = existing_client_id
        else:
            client_id = input("Enter your Discord app client ID: ")
    else:
        client_id = input("Enter your Discord app client ID: ")
else:
    client_id = input("Enter your Discord app client ID: ")


save_option = input("Do you want to save this client ID to a file? (y/n): ").lower()
if save_option == 'y':
    with open(file_path, 'w') as file:
        file.write(client_id)
    print(f"Client ID saved to {file_path}")
else:
    print("Client ID not saved.")
    
RPC = Presence(client_id)
RPC.connect()
print("running. . .")

while True:
    open_tabs = get_unique_window_titles()
    print(open_tabs)
    search_query = process_array(open_tabs)
    print (search_query)
    print(type(search_query))
    gifs_links = get_first_gif_src(search_query)
    print(gifs_links)
    print("------------------------")
    print("And... Online!")
    update_rpc(gifs_links)

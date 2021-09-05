from booking.app import Booking


class Main:
    try:
        with Booking() as bot:
            bot.land_first_page()
            bot.change_currency()
            bot.language(lang="en-gb")
            bot.select_place_to_go(input("\nWhere do u wanna go?: "))   # "NEW YORK"
            

            print("\nFormat: YYYY-MM-DD" ) 
            bot.calendar(
                check_in=input("Enter the checkin Date: "),  # "2021-09-10"
                check_out=input("\nEnter the checkout Date: ")  # "2021-09-16"
                )
            
            bot.select_adults(int(input("\nNo. of people: ")))
            bot.click_search()
            bot.apply_filtrations()
            bot.refresh()   # a workaround to let the bot to grab the data properly
            bot.report_results()
            bot.quit()
            print("\nCompleted!")
            
            
    except Exception as e:
        if 'in PATH' in str(e):
            print(
                "You're tryna run the bot from commad terminal\n"
                "Please add to PATH your Selenium Drivers \n"
                "Windows: \n"
                "   set PATH=%PATH%;C:path-to-your-folder \n\n"
                "Linux: \n"
                "   PATH=$PATH:/path/toyour/folder/ \n"
            )
        else:
            raise
        
if __name__ == "__main__":
    Main()
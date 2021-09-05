from booking.app import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency()
        bot.language(lang="en-gb")
        bot.select_place_to_go("New York")
        
        bot.calendar(check_in="2021-09-20", check_out="2021-09-27")
        
        bot.select_adults(2)
        bot.click_search()
        bot.apply_filtrations()
        # bot.quit()
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
    
    
from booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.select_place_to_go('New York')
    bot.select_dates()
    bot.select_adults(1)
    bot.click_search()

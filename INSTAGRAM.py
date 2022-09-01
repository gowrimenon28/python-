from instabot import Bot
bot=Bot()
bot.login(username="dhavalsays",password="")

followers=bot.get_user_followers("dhavalsays")
for follower in followers:
    print(bot.get_user_info(follower))

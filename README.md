# Nyu </br>
## Discord Bot</br>
[![Discord Bots](https://discordbots.org/api/widget/426047120781344768.svg)](https://discordbots.org/bot/426047120781344768)</br>
A basic Chatting and reminder Bot can send reminder at specified interval of time also can chat with you..</br>
**BOT PREFIX**
> $

Commands and Functions</br></br>
__**For Chatting**__</br>
```
$c(Your message)

Example:

$cHi Nyu
```

</br>

__**For Setting Reminder**__ </br>
```
$reminder_HH:MM:Description #Where HH , MM are number of hours and minutes after you want Bot to send Reminder

Example to send Reminder after 5Hours 40Minutes

$reminder_05:40:ExampleReminder
```

</br>

__**For Translation**__</br>
```
$t Random language 

Example :
$t Hallo, Wie gehts .!
```

</br>

__**For Help**__</br>
```
$help
```


__**About Me**__</br>
```
$AboutMe
```
**For Alarm**</br>
```
$alarm_HH:MM:Name:repetation
```
Note </br>
Here Repetation is a number with digits from 1-7 .Each digit represents week day .</br>
1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday
</br>

For Example to set Alarm at 17:20(UTC/GMT time zone) which repeat on Thursday and Saturday everyweek</br>

```
$alarm_17:20:Example:46
```
Also all time should be in **UTC/GMT time and 24H format** to know current UTC/GMT time just type **$alarm_**.
</br>
**For getting list of alarms on a particular server and get the ALARM ID**</br>
```
$list_alarm
```
**Delete Alarms**</br>
```
$delete_alarm [ALARM ID]
``` 
</br>

---

__**For Random action you want to do on second person eg kiss,lick,slap etc etc**__</br>
```
$a_lick @MentionUser

Example :
@a_kiss @Nyu
```

Package used 
> discord.py

Make a Discord Server 
>https://discordapp.com/

Create an App and bot Account 
>https://discordapp.com/developers/applications/me </br>
>Save Client ID and token

Authorize the bot for your server
>https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot</br>
>XXXXXXXXXXXX is your Client ID 

How to set up

```
pip install discord.py
```
Or
```
python -m pip install discord.py
```

API Wrapper 
>https://github.com/Rapptz/discord.py

API Reference for discord.py
>http://discordpy.readthedocs.io/en/latest/api.html

API for GIFs in action function
>https://tenor.com/ 


**_ThankYou_**

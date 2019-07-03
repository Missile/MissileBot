# MissileBot
A Reddit reply bot.

When the bot account is mentioned (e.g. /u/MissileBot), the message will go into the bot's inbox as a new message. The message will be checked for keywords and matched to a response message. The bot will reply with the message, if there is a keyword match, to the submission/comment that a user had mentioned the bot on.

### Design
| Function | Usage |
| --- | --- |
| bot_login() | Retrieves account login information in an imported file. |
| get_parent() | Retrieves the 'parent' submission/comment identifier to reply to. |
| get_message() | Searches for a keyword in the message and retrieves the response message. |
| reply_mention() | Reads the inbox message, handles the reply message, and allows the bot administrators to delete a submitted message if the bot was wrongly used. |

## Source code
* Any kind of contribution is welcome
* Contact [@Missile](https://reddit.com/user/Missile1337) for support or with suggestions.

# Telegram Group Music Player Bot🎵

## Requirements 📝
- [FFmpeg](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git)
- [python-nodejs](https://hub.docker.com/r/nikolaik/python-nodejs)
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Commands 🛠
- For all in group
   - `/play <reply/url/song>` - Play song you requested
   - `/song <song>` - Download songs you want
   - `/search <query>` - Search videos on youtube with details
   - `@botusername <query>` - Get youtube url by inline
- Admins only
   - `/pause` - Pause song play
   - `/resume` - Resume song play
   - `/skip` - Play next song
   - `/end` - Stop music play
   - `/cleandb` - Clear all files
   - `/userbotjoin` - Add assistant
   - `/userbotleave` - Remove assistant
- Sudo & Owner only
   - `/restart` - Restart bot
   - `/gcast <text/reply>` - Broadcast to groups (auto pinned)
   - `/broadcast <text>` - Broadcast to groups (without pinned)
   - `/exec <code>` - Excute a code
   - `/userbotleaveall` - remove assistant of all groups

## Deploy To Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/galihpujiirianto/MusicManagerBot/tree/main)
+ Recomended use Europe server for deploy on Heroku

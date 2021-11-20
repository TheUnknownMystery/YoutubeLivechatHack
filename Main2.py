import pytchat

#updated on 11/20/2021
chat = pytchat.create(video_id="Please Put you link here")
chat_alive = chat.is_alive()
while chat_alive:
    for c in chat.get().sync_items():

        message = f"{c.message}"
        print('This is a message: ' + message)

        if(message == "!Buy" and message == "!buy"):
            print("!Bought")
        elif(message == "!Sold"):
            print("!Sold")

import pytchat

chat = pytchat.create(video_id="bmVKaAV_7-A")

while chat.is_alive():
    for c in chat.get().sync_items():

        message = f"{c.message}"
        print('This is a message: ' + message)

        if(message == "!Buy" and message == "!buy"):
            print("!Bought")
        elif(message == "!Sold"):
            print("!Sold")

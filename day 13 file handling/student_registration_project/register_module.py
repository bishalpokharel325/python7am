def register(id,username,password,email,phoneno):
    try:
        writer=open("record.csv","a")
        writer.write(f"\n{id},{username},{password},{email},{phoneno}")
        writer.close()
    except Exception as e:
        print(e)


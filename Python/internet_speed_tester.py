import speedtest
bin = []
while len(bin) < 100:
    st = speedtest.Speedtest()
    option = int(input("""
    What speed do you want to test:
    1) Download Speed
    2) Upload Speed
    3) Ping

    Your Choice: """))

    if option == 1:
        x = st.download()
        print(f"{round((x/1000000),3)} megabytes per second")
        bin.append(x)
    elif option == 2:
        x= st.upload()
        print(f"{round((x/1000000),3)} megabytes per second")
        bin.append(x)
    elif option == 3:
        servernames = []
        st.get_servers(servernames)
        print(st.results.Ping)

    else:
        print("Please enter the correct choice.")
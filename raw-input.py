a = raw_input("Enter any message")
file = open("doc.txt", "w")
file.write("Show Entered message : " + a +"\n")
file.close()

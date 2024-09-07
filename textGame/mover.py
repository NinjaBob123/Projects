import os
os.mkdir("C:/Users/littl/OneDrive/PycharmProjects")
os.mkdir("C:/Users/littl/OneDrive/PycharmProjects/textGame")
for file in os.listdir("C:/Users/littl/PycharmProjects/textGame"):
    os.rename(f"C:/Users/littl/PycharmProjects/textGame/{file}", f"C:/Users/littl/OneDrive/PycharmProjects/textGame/{file}")
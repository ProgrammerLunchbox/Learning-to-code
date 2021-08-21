import random

temperature = int(input("What's the weather like in you're area?"))
username = input("What is your name?")
fahrenheit = temperature


celsius = ((fahrenheit-32)*5/9)

if temperature <= 35:
    print("Brrrr its cold outside, Dont forget your jacket okay!")
    print("In fahrenheit the temp is:")
    print(fahrenheit)
    print("In celsius the temp is:")
    print(round(celsius, 1))

elif temperature >= 55:

    print("Oh boy it's hot outside! Leave the jacket and bring the sun screen!")
    print("In fahrenheit the temp is:")
    print(fahrenheit)
    print("In celsius the temp is:")
    print(round(celsius, 1))
elif int(temperature) in range(36, 54):
    print("The weather is mild so use your own personal discretion when choosing your outfit today!")
    print("In fahrenheit the temp is:")
    print(fahrenheit)
    print("In celsius the temp is:")
    print(round(celsius, 1))

print("Have an amazing day today", username)

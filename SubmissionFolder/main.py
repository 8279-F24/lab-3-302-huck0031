from adafruit_circuitplayground import cp

while True:
    orange = (253, 108, 7)
    ledOff = (0, 0, 0)
    # Prompt user for the number of LEDs
    try:
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
    except ValueError:
        print("Inserted value is not a number.")
        continue
    
    # Check if the number is within the valid range
    if 1 <= num_leds <= 10:
        # Turn off all LEDs
        for j in range(0, 10):
            cp.pixels[j] = ledOff
        # Turn on LEDs using a for loop
        for i in range(0, num_leds):
            print(f"LED {i} is ON")
            cp.pixels[i] = orange
    else:
        print("Number out of range. Please enter a number between 1 and 10.")
        continue
    
    # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        print("Program ended.")
        break
    

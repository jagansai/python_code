when taking **`input`** from the prompt, we get the input in the form of text / string.

For e.g., if the prompt says `Enter number: 4`
Here `4` is returned in the form of **text**. It can't be treated like a **number** unless it is converted to a **number**.

To convert that to a number, we should cast it to a number.
It can be done like below.
```
number = input("Enter number: ")
number = int(number)
```

Always remember that only proper **numbers** can be converted from **text** to **numbers**

For example, below code returns you incorrect value if converted from **text** to **number**

```
number = "10, "
number = int(number) # 👈🏼 results in an error that says, invalid literal for int() with base 10: '4 ,'
```


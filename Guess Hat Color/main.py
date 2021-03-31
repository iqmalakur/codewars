def guess_hat_color(a,b,c,d):
    return 1 if b == c else 2

print(guess_hat_color("white", "black", "white", "black"), "->", 2)
print(guess_hat_color("white", "black", "black", "white"), "->", 1)
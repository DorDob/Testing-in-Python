def biggest_common_divisor(x, y):
   while x != y:
       x, y = max(x, y), min(x, y)
       x = x - y
   return x

if __name__ == "__main__":
    result = biggest_common_divisor(75,5)
    print (result)
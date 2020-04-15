#rules for all hash functions
    #output must be deterministic- 
    #defind output range
    # predictable speed
    # Non invertable
import time

input_string = b"apple"
n = 1000000

print(f"Hashing (n)x")

start_time = time.time()
for i in range(n):
    output_hash = hash(input_string)

end_time = time.time()
print(output_hash)

# Hash Tables = dictonares
#  takes only a string as KeyError
#     1. has the key and get the num in some range
#         length of an array - need the num % length
#     2. store/ retrieve value at that hashed number


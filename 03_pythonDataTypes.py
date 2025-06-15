# Text Type         :	str
# Numeric Types     :	int, float, complex
# Sequence Types    :	list, tuple, range
# Mapping Type      :	dict
# Set Types         :	set, frozenset
# Boolean Type      :	bool
# Binary Types      :	bytes, bytearray, memoryview
# None Type         :	NoneType

# data types
print(type("Hello World"),
      type(20),
      type(20.5),
      type(1j),
      type(['apple', 'banana']),
      type(('apple', 'banana')),
      type(range(6)),
      type({"name" : "john", "age" : 36}),
      type({'apple', 'banana'}),
      type(frozenset({'apple', 'banana'})),
      type(True),
      type(None)
      )

x = b"Hello"
y = bytearray(5)
z = memoryview(bytes(5))
print(x, y, z)
print(type(x), type(y), type(z))
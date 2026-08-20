import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o-mini")

samples = [
    "I want to block my debit card immediately",
    "मेरा डेबिट कार्ड खो गया है",                      # Hindi
    "Mera card kho gaya hai, please block karo",       # Hinglish
    "Account number 3021 4456 8890 1123",
    "Please transfer five thousand rupees to my savings account",
    "मुझे अपने बचत खाते में पैसे भेजने हैं",
]
for s in samples:
    tokens = enc.encode(s)
    print(f"{len(tokens):>3} tokens -> {s}")




# Task 1.1 — See Tokens With Your Own Eyes

## Tokenization Results

|  # | Language | Sentence                                                   | Tokens |
| -: | -------- | ---------------------------------------------------------- | -----: |
|  1 | English  | I want to block my debit card immediately                  |      8 |
|  2 | Hindi    | मेरा डेबिट कार्ड खो गया है                                 |      9 |
|  3 | Hinglish | Mera card kho gaya hai, please block karo                  |     10 |
|  4 | English  | Account number 3021 4456 8890 1123                         |     14 |
|  5 | English  | Please transfer five thousand rupees to my savings account |     10 |
|  6 | Hindi    | मुझे अपने बचत खाते में पैसे भेजने हैं                      |     11 |

## (a) Why did the Hindi sentence produce more tokens than the English one?

In my experiment, the first Hindi sentence used 9 tokens, while the English sentence used 8 tokens.

This happens because a token is not always the same as a word. The tokenizer breaks a sentence into smaller pieces that the model understands. Some English text can be represented using fewer pieces, while some Hindi text may need more pieces.

However, this does **not** mean Hindi always uses more tokens than English. My results show this clearly:

* English sentences: 8, 14, and 10 tokens
* Hindi sentences: 9 and 11 tokens
* Hinglish sentence: 10 tokens

So, the number of tokens depends on the **actual sentence**, not just the language.

## (b) What does this mean for the cost and latency of a multilingual bot?

More tokens mean that the model has more text to process.

For a bank chatbot, this can mean:

* **More tokens = potentially higher cost**
* **More tokens = potentially more processing time**
* **More tokens = more space used in the model's context**

For example, if two customers send messages that mean almost the same thing, but one message requires more tokens, the model may need to process more input for that message.

Therefore, when building a multilingual banking bot, we should test real messages in different languages and check how many tokens they use.

## (c) What happened to the account number?

The account-number sentence used **14 tokens**, which was the highest result in my experiment.

```text
Account number 3021 4456 8890 1123
```

To us, this looks like four groups of four numbers.

But the tokenizer does not necessarily see it as four simple pieces. It can break the numbers into smaller pieces.

This is why the account number used 14 tokens.

This also shows that numbers and account IDs can sometimes use more tokens than we expect.

## Cost Exercise

I measured these six token counts:

```text
8 + 9 + 10 + 14 + 10 + 11 = 62
```

Average tokens per customer message:

```text
62 / 6 = 10.33 tokens
```

The bank receives 50,000 messages every day:

```text
50,000 × 10.33
≈ 516,667 tokens/day
```

For 30 days:

```text
516,667 × 30
≈ 15,500,000 tokens/month
```

GPT-4o mini input pricing is **$0.15 per 1 million input tokens**.

Therefore:

```text
15,500,000 / 1,000,000
= 15.5 million tokens

15.5 × $0.15
= $2.325
```

So the estimated monthly input cost is approximately:

**$2.33 per month**

This is only the **input cost**. It does not include output tokens or other API costs.

Your version is already correct. I would make it slightly clearer and more natural:

## Key Takeaway

I learned that an LLM does not read text exactly like a human. It first breaks the text into smaller pieces called **tokens**. One word can sometimes be represented by one token, while another word can be split into multiple tokens.

Different languages, numbers, and types of sentences can use different numbers of tokens. My experiment showed that token count depends on the actual text, not only on the language.

More tokens can mean higher input costs and potentially more processing time. Therefore, understanding tokenization is important when building and scaling a multilingual chatbot.

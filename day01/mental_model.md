
# Three Quiz Questions

### **Question 1: Why can an LLM confidently provide information about something that does not actually exist?**

The model's job is just to guess the next word (token) that sounds most likely, based on patterns it saw in training. It doesn't have a step where it checks "is this actually true?" So when you asked about a fake credit card, the model had seen many *real* credit card descriptions before. It used that pattern to make up a fee and benefits that *sound* real — even though they're not. It sounds confident because it's just really good at sounding fluent, not because it "knows" the answer is correct. That's why it hallucinates: it mixes up "sounds right" with "is right."

### **Question 2: Why is an external tool or retrieval system useful when an LLM needs to answer a question about current information?**

Two simple reasons:
1. The model only knows what it was trained on, up to a certain date (its "knowledge cutoff"). It can't know about anything newer, like today's RBI repo rate.
2. Even when it doesn't know something, it might guess instead of saying "I don't know" — like you saw in your experiment.

So tools like search or live APIs fetch the real, current answer and give it to the model directly. Then the model just has to read and repeat that correct information, instead of guessing from memory.

### **Question 3: What is the difference between what a model learns during pretraining and what post-training adds?**

- **Pretraining** teaches the model to predict the next word using tons of internet text. This is where it picks up language, facts, and general knowledge. But it only knows how to "continue text" — it doesn't know how to have a conversation or follow instructions properly.
- **Post-training** teaches the model *how to behave* like a helpful assistant — how to answer questions directly, follow instructions, and refuse bad requests. It doesn't add new facts, it just teaches the model good habits for talking to people.

Simple way to remember it: **pretraining = knowledge, post-training = manners.**
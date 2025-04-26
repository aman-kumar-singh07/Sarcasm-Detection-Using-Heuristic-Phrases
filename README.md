This is a extention of Yelp Business Reviews 
What I am doing?
I am solving one of  the most challenging problems that we face in sentiment analyses of  customer reviews i.e, Sarcastic reviews. 

How I am doing it?
1. TextBlob Analysis (Emotional Tone)
It checks the polarity (how positive/negative) and subjectivity (how opinionated) of the text.

Example: "Just loved getting food poisoning" → gets high positive polarity because of the word “loved”.

2. Manual Pattern Spotting (Heuristic Detection)
You’ve created 3 key rules to “catch” sarcasm:

The 3 Sarcasm Detection Traps:
1. Conflict Between Positive and Negative Words
Checks if both positive cues (like love, great) and negative cues (not, never, food poisoning, nothing) exist in the same sentence.
If yes → sarcasm_score += 1 ✅

2. Use of Sarcastic Tone Markers (Emojis & Punctuation)
Catches sarcastic flair like:
!!!, 🙄, 😒, lol, wow, ...
If found → sarcasm_score += 1 ✅

3. Specific Trigger Words (Dark Humour Examples)
Looks for phrases that are clearly bad but appear in “positive sentences”, like:
food poisoning, worst
These boost your sarcasm score.

Final Decision:
return sarcasm_score >= 2  or  return sarcasm_score >= 1 (a/b test)
Also, in different versions of codes I have tried without trigger words also, but it's not possible to fine tune  without machine learning models because trigger words could be 100. Possibilities could be too many, we cannot hard code it.

→ So I declare a sentence sarcastic only if 2 or more traps are triggered.
Then You Flip the Sentiment!
If sarcasm is detected, and TextBlob said it's “Positive” → you flip it to Negative because it's probably sarcastic.

Example:
"Just loved getting food poisoning. Best birthday ever!!!"

love, best → positive cue
food poisoning → negative phrase
!!! → sarcastic indicator

So sarcasm_score = 3 → sarcastic = True
Then your code flips Positive → Negative to get the final sentiment.

Output : Enter your review sir : Just loved getting food poisoning. Best birthday ever!!!
final_sentiment: Negative
polarity: 0.85
subjectivity: 0.55
sarcastic: True

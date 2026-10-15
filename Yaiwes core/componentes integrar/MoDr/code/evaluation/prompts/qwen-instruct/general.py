system_prompt = "Please reason step by step, and put your final answer within \\boxed{}."

few_shot_prompt = ""

question_format = """{question}"""

system_nl_with_input_prompt = "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request. "

system_nl_without_input_prompt = "Below is an instruction that describes a task. Write a response that appropriately completes the request. "

question_format_with_input = """### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"""

question_format_without_input = """### Instruction:\n{instruction}\n\n### Response:"""


gpqa_few_shot_prompt = """## Examples:
### Instruction:
Please choose the correct answer to the question: Which piece of safety equipment is used to keep mold spores from entering the respiratory system?

Answer1: safety goggles Answer2: breathing mask Answer3: rubber gloves Answer4: lead apron

Answer format: answer1/answer2/answer3/answer4

### Response:
the correct answer is answer2


## Instruction:
Please choose the correct answer to the question: Which characteristic describes the texture of a kitten's fur?

Answer1: gray Answer2: warm Answer3: long Answer4: soft

Answer format: answer1/answer2/answer3/answer4

### Response:
the correct answer is answer4


## Instruction:
Please choose the correct answer to the question: Plants use sunlight to make

Answer1: soil. Answer2: minerals. Answer3: food. Answer4: water.

Answer format: answer1/answer2/answer3/answer4

### Response:
the correct answer is answer3


"""


math_few_shot_prompt = """## Examples:
Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Answer: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6. Therefore, the answer is \\boxed{6}.

Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
Answer: There are 3 cars in the parking lot. 2 more cars arrive. So there are 3 + 2 = 5 cars in the parking lot. Therefore, the answer is \\boxed{5}.

Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
Answer: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. Therefore, the answer is \\boxed{39}.

Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Answer: Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8. Therefore, the answer is \\boxed{8}.

Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Answer: Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9. Therefore, the answer is \\boxed{9}.

Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
Answer: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. Therefore, the answer is \\boxed{29}.

Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
Answer: Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls. Therefore, the answer is \\boxed{33}.

Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
Answer: Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8. Therefore, the answer is \\boxed{8}.


"""

multiple_choice_few_shot_prompt = """## Examples:
Question: If f(b)=b^2 and b is a positive integer, which of the following CANNOT be the value of f(f(b))? The options are: A)1, B)81, C)200, D)256, E)625
Answer: To solve this problem, f(b)=b^2\nf(f(b)) = (b^2)^2 = b^4\nTherefore f(f(b)) will be numbers that are 4th power of other numbers.\nChecking the options:\n1 = 1^$\n81 = 3^4\n200. This cannot be written as the 4th power of any number\n256 = 4^4\n625 = 5^4\n\nThe correct answer is \\boxed{C}.

Question: I walk a certain distance and ride back taking a total time of 37 minutes. I could walk both ways in 55 minutes. How long would it take me to ride both ways? The options are: A)12 mins, B)10 mins, C)19 mins, D)15 mins, E)20 mins
Answer: Let the distance be x km. Then,\n( Time taken to walk x km) + (time taken to ride x km) =37 min.\n( Time taken to walk 2x km ) + ( time taken to ride 2x km )= 74 min.\nBut, the time taken to walk 2x km = 55 min.\nTime taken to ride 2x km = (74-55)min =19 min.\n\nThe correct answer is \\boxed{C}.

Question: It is well known that a triangle's area is \u221a(p(p-a)(p-b)(p-c)), when p=(a+b+c)/2, such that a, b, c are the lengths of sides of the triangle. If the triangle has 300, 300, and 300 as the side's lengths, what is the triangle's area? The options are: A)34,200, B)36,200, C)38,200, D)42,200, E)38,971
Answer: It is well known that a triangle's area is \u221a(p(p-a)(p-b)(p-c)), when p=(a+b+c)/2,\n-> P=(300+300+300)/2=450, area=\u221a(450(450-300)(450-300)(450-300))=38,971. Therefore, the answer is \\boxed{E}.

Question: The price of a car and AC are in the ratio 3:2. If the scooter costs $500 more than the AC. then the price of the AC? The options are: A)1500, B)200, C)1700, D)2000, E)2500
Answer: Let the price of the Car and AC is 3x and 2x\n3x-2x = 500\nx = 500\nPrice of AC = 3*500 = $1500\n\nThe correct answer is \\boxed{A}.

Question: What is the difference between the place value of 1 in the numeral 7119? The options are: A)150, B)160, C)180, D)90, E)210
Answer: 100 - 10 = 90\n\nThe correct answer is \\boxed{D}.

Question: Before a salary increase, the weekly salary of a worker for 42 hours in a week was as much as the worker is paid now for 40 hours of work in a week. What is the percent increase in the worker's salary per hour? The options are: A)3, B)4, C)5, D)6, E)7
Answer: Let x be the original salary per hour.\nLet y be the salary per hour after the increase.\n40y=42x\ny=(42/40)x=1.05x\nThe salary increased 5%.\n\nThe correct answer is \\boxed{C}.

Question: what is the sum of the first 18 odd natural numbers? The options are: A)300, B)400, C)500, D)324, E)700
Answer: sum of first n odd natural nuber is = n^2\nso sum of the first 18 odd natural numbers=(18)^2=324\nans 324\nANSWER:D\n\nThe correct answer is \\boxed{D}.

Question: John was 19 years old when he married Betty. They just celebrated their fifth wedding anniversary, and Betty's age is now 7/8 of John's. How old is Betty? The options are: A)21, B)26, C)28, D)30, E)32
Answer: Assume Betty's age on marriage = x years.\nJohn's age on marriage = 19\nJohn's age after 5 years = 24 years.\nBetty's age after 5 years = x + 5\nGiven: x + 5 = 7/8 (24) = 21\nTherefore Betty's current age = 21\nOption A\n\nThe correct answer is \\boxed{A}.


"""
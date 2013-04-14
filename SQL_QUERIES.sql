SQL QUERIES FOR WORD FLASH

mysql> CREATE TABLE Exercise1 (id INT NOT NULL AUTO_INCREMENT, word CHAR(30) NOT NULL, description CHAR(100) NULL, PRIMARY KEY (id));
Query OK, 0 rows affected (0.10 sec)

CREATE TABLE Exercises (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
Exercise VARCHAR(50), Description VARCHAR(500))

CREATE TABLE Science (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
Word VARCHAR(50))

INSERT INTO Exercises (Exercise, Description) VALUES ('Science', 'Contains all the scientific words')

CREATE TABLE Schedule (id INTEGER PRIMARY KEY AUTO_INCREMENT, EventName VARCHAR(50), ScheduleTime VARCHAR(50), Description VARCHAR(100))
    -> ;

INSERT INTO Schedule (EventName,ScheduleTime, Description) VALUES ('Board Meeting', '2012-04-21', 'Meeting to be held')
    -> ;

CREATE TABLE Idea (id INTEGER PRIMARY KEY AUTO_INCREMENT, IdeaName VARCHAR(50), IdeaDate DATETIME, Description VARCHAR(200))

INSERT INTO Idea (IdeaName, IdeaDate, Description) VALUES ('Scientific Journal', 2012-04-21, 'Scientifi Journal on Black hole')


INSERT INTO Schedule (EventName,ScheduleTime, Description) VALUES ('Group Study', '2012-04-21', 'Study for the Exam')

CREATE TABLE Synonyms (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, first_word VARCHAR(30) NOT NULL, second_word VARCHAR(30) NOT NULL)

CREATE TABLE Antonyms (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, first_word VARCHAR(30) NOT NULL, second_word VARCHAR(30) NOT NULL)

CREATE TABLE Sentences (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, sentence VARCHAR(30) NOT NULL, word VARCHAR(30) NOT NULL)

CREATE TABLE Sentences (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, sentence VARCHAR(30) NOT NULL, 
	optionone VARCHAR(30) NOT NULL, optiontwo VARCHAR(30) NOT NULL, optionthree VARCHAR(30) NOT NULL, optionfour VARCHAR(30) NOT NULL)
	
CREATE TABLE LBL_Sentences (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, sentence VARCHAR(30) NOT NULL, 
	optionone VARCHAR(30) NOT NULL, optiontwo VARCHAR(30) NOT NULL, optionthree VARCHAR(30) NOT NULL, optionfour VARCHAR(30) NOT NULL)

CREATE TABLE LAL_Sentences (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, sentence VARCHAR(30) NOT NULL, 
	optionone VARCHAR(30) NOT NULL, optiontwo VARCHAR(30) NOT NULL, optionthree VARCHAR(30) NOT NULL, optionfour VARCHAR(30) NOT NULL,
	optionfive VARCHAR(30) NOT NULL)


INSERT INTO Sentences (sentence, word) VALUES ('The boy scored the highest marks in the class, He is a - boy', 'Clever')
INSERT INTO Sentences (sentence, word) VALUES ('The kid breaks the things at home and scatters it, He is - kid', 'naughty')
INSERT INTO Sentences (sentence, word) VALUES ('The woman does a lot of shopping with a very less salary, She is - ', 'Spendthreft')
INSERT INTO Sentences (sentence, word) VALUES ('The Man broke the iron gate, He is a - man', 'Strong')
INSERT INTO Sentences (sentence, word) VALUES ('The teacher shouted at the students, She was in a - mood', 'bad')

INSERT INTO suppliers
(supplier_id, supplier_name)
SELECT account_no, name
FROM customers
WHERE city = 'Newark';

INSERT INTO LAL_Sentences (sentence, optionone, optiontwo, optionthree, optionfour, optionfive) 
SELECT sentence, optionone, optiontwo, optionthree, optionfour, optionfive  FROM HIL_Sentences WHERE Id BETWEEN 161 AND 171


CREATE TABLE LAL_Sentences (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, sentence VARCHAR(30) NOT NULL, 
	optionone VARCHAR(30) NOT NULL, optiontwo VARCHAR(30) NOT NULL, optionthree VARCHAR(30) NOT NULL, optionfour VARCHAR(30) NOT NULL,
	optionfive VARCHAR(30) NOT NULL)	

INSERT INTO Synonyms (first_word, second_word) VALUES ('Clever', 'Smart')

INSERT INTO Synonyms (first_word, second_word) VALUES ('disturbance', 'agitation'),
('complexity', 'entanglement'),
('trivial', 'insignificant'),
('brave', 'adventurous'),
('big', 'large'),
('blank', 'empty'),
('fertile', 'fruitful'),
('false', 'untrue'),
('loving', 'fond'),
('usual', 'normal'),
('thin', 'lean'),
('safe', 'secure'),
('sleepy', 'drowsy')

CREATE TABLE Passages (passage VARCHAR(30) NOT NULL)

CREATE TABLE Passages (passage_title VARCHAR(30) NOT NULL, passage_tablename VARCHAR(30) NOT NULL)

INSERT INTO Passages (passage_title, passage_tablename) VALUES ('Reading Comprehension 1', 'Comprehension 1')

CREATE TABLE PassageContent (passage_content BLOB, passage_tablename VARCHAR(30) NOT NULL)

INSERT INTO PassageContent (passage_content, passage_tablename) VALUES ('The word euthanasia is of Greek origin and literally means “a good death.” 
The American Heritage Dictionary defines it as “the act of killing a person painlessly for reasons of mercy.” 
Such killing can be done through active means, such as administering a lethal injection, or by passive means, such as withholding medical care or food and water.

In recent years in the United States, there have been numerous cases of active euthanasia in the news. 
They usually involve the deliberate killing of ill or incapacitated persons by relatives or friends who plead that they can no longer bear to see their loved ones suffer. 
Although such killings are a crime, the perpetrators are often dealt with leniently by our legal system, and the media usually portrays them as compassionate heroes who take personal risks to save another from unbearable suffering. 

The seeming acceptance of active forms of euthanasia is alarming, but we face a bigger, more insidious threat from passive forms of euthanasia. 
Every year, in hospitals and nursing homes around the country, there are growing numbers of documented deaths caused by caregivers withholding life-sustaining care, including food and water, from vulnerable patients who cannot speak for themselves.

While it is illegal to kill someone directly, for example with a gun or knife, in many cases the law has put its stamp of approval on causing death by omitting needed care. Further, many states have “living will” laws designed to protect those who withhold treatment, 
and there have been numerous court rulings which have approved of patients being denied care and even starved and dehydrated to death.

Because such deaths occur quietly within the confines of hospitals and nursing homes, they can be kept hidden from the public. 
Most euthanasia victims are old or very ill, so their deaths might be attributed to a cause other than the denial of care that really killed them. 
Further, it is often relatives of the patient who request that care be withheld. In one court case, the court held that decisions to withhold life-sustaining care may be made not only by close family members but also by a number of third parties, and that such decisions need not be reviewed by the judicial system if there is no disagreement between decision makers and medical staff. The court went so far as to rule that a nursing home may not refuse to participate in the fatal withdrawal of food and water from an incompetent patient!

“Extraordinary” or “heroic” treatment need not be used when the chance for recovery is poor and medical intervention would serve only to prolong the dying process. But to deny customary and reasonable care or to deliberately starve or dehydrate someone because he or she is very old or very ill should not be permitted. Most of the cases coming before the courts do not involve withholding heroic measures from imminently dying people, but rather they seek approval for denying basic care, such as administration of food and water, to people who are not elderly or terminally ill, but who are permanently incapacitated. These people could be expected to live indefinitely, though in an impaired state, if they were given food and water and minimal treatment.
No one has the right to judge that another’s life is not worth living. The basic right to life should not be abridged because someone decides that someone else’s quality of life is too low. If we base the right to life on quality of life standards, there is no logical place to draw the line.

To protect vulnerable patients, we must foster more positive attitudes towards people with serious and incapacitating illnesses and conditions. Despite the ravages of their diseases, they are still our fellow human beings and deserve our care and respect. We must also enact
positive legislation that will protect vulnerable people from those who consider their lives meaningless or too costly to maintain and who would cause their deaths by withholding life-sustaining care such as food and water.', 'Comprehension1')


INSERT INTO PassageContent (passage_content, passage_tablename) VALUES ('The word euthanasia is of Greek origin and literally means “a good death.”  The American Heritage Dictionary defines it as “the act of killing a person painlessly for reasons of mercy.” Such killing can be done through active means, such as administering a lethal injection, or by passive means, such as withholding medical care or food and water. In recent years in the United States, there have been numerous cases of active euthanasia in the news. 

They usually involve the deliberate killing of ill or incapacitated persons by relatives or friends who plead that they can no longer bear to see their loved ones suffer. Although such killings are a crime, the perpetrators are often dealt with leniently by our legal system, and the media usually portrays them as compassionate heroes who take personal risks to save another from unbearable suffering. 

The seeming acceptance of active forms of euthanasia is alarming, but we face a bigger, more insidious threat from passive forms of euthanasia. Every year, in hospitals and nursing homes around the country, there are growing numbers of documented deaths caused by caregivers withholding life-sustaining care, including food and water, from vulnerable patients who cannot speak for themselves. While it is illegal to kill someone directly, for example with a gun or knife, in many cases the law has put its stamp of approval on causing death by omitting needed care. Further, many states have “living will” laws designed to protect those who withhold treatment, 
and there have been numerous court rulings which have approved of patients being denied care and even starved and dehydrated to death. Because such deaths occur quietly within the confines of hospitals and nursing homes, they can be kept hidden from the public.

Most euthanasia victims are old or very ill, so their deaths might be attributed to a cause other than the denial of care that really killed them. Further, it is often relatives of the patient who request that care be withheld. In one court case, the court held that decisions to withhold life-sustaining care may be made not only by close family members but also by a number of third parties, and that such decisions need not be reviewed by the judicial system if there is no disagreement between decision makers and medical staff. The court went so far as to rule that a nursing home may not refuse to participate in the fatal withdrawal of food and water from an incompetent patient! “Extraordinary” or “heroic” treatment need not be used when the chance for recovery is poor and medical intervention would serve only to prolong the dying process. But to deny customary and reasonable care or to deliberately starve or dehydrate someone because he or she is very old or very ill should not be permitted. 

Most of the cases coming before the courts do not involve withholding heroic measures from imminently dying people, but rather they seek approval for denying basic care, such as administration of food and water, to people who are not elderly or terminally ill, but who are permanently incapacitated. These people could be expected to live indefinitely, though in an impaired state, if they were given food and water and minimal treatment.

No one has the right to judge that another’s life is not worth living. The basic right to life should not be abridged because someone decides that someone else’s quality of life is too low. If we base the right to life on quality of life standards, there is no logical place to draw the line.

To protect vulnerable patients, we must foster more positive attitudes towards people with serious and incapacitating illnesses and conditions. Despite the ravages of their diseases, they are still our fellow human beings and deserve our care and respect. We must also enact
positive legislation that will protect vulnerable people from those who consider their lives meaningless or too costly to maintain and who would cause their deaths by withholding life-sustaining care such as food and water.', 'Comprehension1')

CREATE TABLE Passages List (passage VARCHAR(30) NOT NULL)

CREATE TABLE QuestionsTable (passage_tablename VARCHAR(30) NOT NULL, question VARCHAR(2000) NOT NULL, optionone VARCHAR(2000) NOT NULL,
optiontwo VARCHAR(2000) NOT NULL, optionthree VARCHAR(2000) NOT NULL, optionfour VARCHAR(2000), optionfive VARCHAR(2000))

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, optionfour, optionfive) 
VALUES (')



INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
('Comprehension1', 'As used in paragraph 7, which is the best definition of abridged?',
'trimmed','curtailed','lengthened','exteneded','compressed')

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
('Comprehension1', 'The main idea of paragraph 7 is that',
"using a subjective standard will make the decision to end an individual's life arbitrary",
"lawyers will be unable to prosecute or defend caregivers",
"no comprehensive right or wrong definition of euthanasia will exist",
"no boundary will exist between euthanasia and care omission",
"quality of life will no longer be able to be rigidly defined")


INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension1", 'In the final paragraph the author writes, 
"Despite the ravages of their diseases, they are still our fellow human beings and deserve our care and respect." 
The main purpose of this statement is to',
"justify an earlier statement",
"prove a previous argument",
"illustrate an example",
"gainsay a later statement",
"object to a larger idea")


INSERT INTO PassageContent (passage_content, passage_tablename) VALUES ('Concussions are brain injuries that occur when a person receives a blow to the head, face, or neck. Although most people who suffer a concussion experience initial bouts of dizziness, nausea, and drowsiness, these symptoms often disappear after a few days. The long-term effects of concussions, however, are less understood and far more severe. Recent studies suggest that people who suffer multiple concussions are at significant risk for developing chronic traumatic encephalopathy (CTE), a degenerative brain disorder that causes a variety of dangerous mental and emotional problems to arise weeks, months, or even years after the initial injury. These psychological problems can include depression, anxiety, memory loss, inability to concentrate, and aggression. In extreme cases, people suffering from CTE have even committed suicide or homicide. The majority of people who develop these issues are athletes who participate in popular high-impact sports, especially football. Although new sports regulations and improvements in helmet technology can help protect players, amateur leagues, the sports media, and fans all bear some of the responsibility for reducing the incidence of these devastating injuries.

Improvements in diagnostic technology have provided substantial evidence to link severe—and often fatal—psychological disorders to the head injuries that players receive while on the field. Recent autopsies performed on the brains of football players who have committed suicide have shown advanced cases of CTE in every single victim.

In response to the growing understanding of this danger, the National Football League (NFL) has revised its safety regulations. Players who have suffered a head injury on the field must undergo a "concussion sideline assessment"—a series of mental and physical fitness tests—before being allowed back in the game. In an effort to diminish the amount of head and neck injuries on the field, NFL officials began enforcing stricter penalty calls for helmet-to-helmet contact, leading with the head, and hitting a defenseless player. Furthermore, as of 2010, if a player’s helmet is accidentally wrenched from his head during play, the ball is immediately whistled dead. It is hoped that these new regulations, coupled with advances in helmet design, will reduce the number of concussions, and thus curb further cases of CTE. 

Efforts by the NFL and other professional sports leagues are certainly laudable; we should commend every attempt to protect the mental and physical health of players. However, new regulations at the professional level cannot protect amateur players, especially young people. Fatal cases of CTE have been reported in victims as young as 21. Proper tackling form—using the arms and shoulders to aim for a player’s midsection—should be taught at an early age. 

Youth, high school, and college leagues should also adopt safety rules even more stringent than those of the NFL. Furthermore, young athletes should be educated about the serious dangers of head injuries at an early age.
Perhaps the most important factor in reducing the number of traumatic brain injuries, however, lies not with the players, the coaches, or the administrators, but with the media and fans. Sports media producers have become accustomed to showcasing the most aggressive tackles and the most intense plays. NFL broadcasts often replay especially violent collisions while the commentators marvel at the players physical prowess. Some sports highlights television programs even feature weekly countdowns of the "hardest hits." When the media exalts such dangerous behavior, professionals are rewarded for injuring each other on the field and amateurs become more likely to try to imitate their favorite NFL athletes. Announcers, commentators, television producers, and sportswriters should engage in a collective effort to cease glorifying brutal plays. In turn, fans should stop expecting their favorite players to put their lives on the line for the purposes of entertainment. Players must not be encouraged to trade their careers, their health, their happiness, and even their lives for the sake of a game.', 'Comprehension2')

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension2", 'Based on information in the passage, it can be inferred that all of the following statements are true except',
"NFL officials have done little to address the problem of CTE",
"tackling is not always dangerous; however, players who use improper tackling form may injure others",
"scientists have established a definitive link between players who die untimely deaths and the onset of CTE",
"athletes who are praised for exceptionally brutal hits are likely to continue engaging in such dangerous behavior",
"the NFL has done more to mitigate future cases of CTE than youth, high school, or college leagues have done")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension2", 'As used in paragraph 3, which is the best synonym for laudable?',
"praiseworthy",
"ineffectual",
"memorable",
"audacious",
"satisfactory")


INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension2", "The author's tone in the final paragraph can best be described as",
"insistent",
"remorseful",
"hopeless",
"perplexed",
"arrogant")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension2", "As used in the final paragraph, which is the best antonym for exalts?",
"castigates",
"mitigates",
"venerates",
"mollifies",
"expedites")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension2", "In describing the sports media, the author emphasizes its",
"sensationalism",
"responsibility",
"entertainment value",
"senselessness",
"danger")

INSERT INTO PassageContent (passage_content, passage_tablename) VALUES ("The biggest house of cards, the longest tongue, and of course, the tallest man these are among the thousands of records logged in the famous Guinness Book of Records. Created in 1955 after a debate concerning Europe's fastest game bird, what began as a marketing tool sold to pub landlords to promote Guinness, an Irish drink, became the bestselling copyright title of all time (a category that excludes books such as the Bible and the Koran). In time, the book would sell 120 million copies in over 100 countries-quite a leap from its humble beginnings.

In its early years, the book set its sights on satisfying man's innate curiosity about the natural world around him. Its two principal fact finders, twins Norris and Ross McWhirter, scoured the globe to collect empirical facts. It was their task to find and document aspects of life that can be sensed or observed, things that can be quantified or measured. But not just any things. They were only interested in superlatives: the biggest and the best. It was during this period that some of the hallmark Guinness Records were documented, answering such questions as 'What is the brightest star?' and 'What is the biggest spider?'

Once aware of the public's thirst for such knowledge, the book's authors began to branch out to cover increasingly obscure, little-known facts. They started documenting human achievements as well. A forerunner for reality television, the Guinness Book gave people a chance to become famous for accomplishing eccentric, often pointless tasks. Records were set in 1955 for consuming 24 raw eggs in 14 minutes and in 1981 for the fastest solving of a Rubik's Cube (which took a mere 38 seconds). In 1979 a man yodeled non-stop for ten and a quarter hours.

In its latest incarnation, the book has found a new home on the internet. No longer restricted to the confines of physical paper, the Guinness World Records website contains seemingly innumerable facts concerning such topics as the most powerful combustion engine, or the world's longest train. What is striking, however, is that such facts are found sharing a page with the record of the heaviest train to be pulled with a beard. While there is no denying that each of these facts has its own, individual allure, the latter represents a significant deviation from the education-oriented facts of earlier editions. Perhaps there is useful knowledge to be gleaned regarding the tensile strength of a beard, but this seems to cater to an audience more interested in seeking entertainment than education.

Originating as a simple bar book, the Guinness Book of Records has evolved over decades to provide insight into the full spectrum of modern life. And although one may be more likely now to learn about the widest human mouth than the highest number of casualties in a single battle of the Civil War, the Guinness World Records website offers a telling glimpse into the future of fact-finding and record-recording.", "Comprehension3")



INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension3", "Which of the following statements would best serve as the headline for this passage?",
"The encyclopedia of the extremes reflects the changing interests of modern society.",
"A book of simple origins makes it to the top as sales total a staggering 120 million copies.",
"Facts are often displayed in a boring, uninteresting manner, but not in the Guinness Book of Records.",
"The Guinness World Records website proves itself a valuable resource for insight into the full spectrum of modern life.",
"Where other books fall short, the index of superlative sciences never ceases to amaze.")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension3", "According to the author, the most significant difference between older editions of the Guinness Book of 
Records and the new Guinness World Records website involves",
"a shift in focus from educational to entertaining material",
"an end to the use of facts as a means to promote Guinness",
"an overall increase in the total number of facts presented",
"a move from fact-finding to the recording of achievements",
"a departure from book sales being limited to local pubs and bars")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension3", "As used in paragraph 2, which is the best definition for empirical?",
"derived from experience",
"natural",
"recordable",
"excellent or unmatched",
"convenient or handy")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension3", "Using the passage as a guide, it can be inferred that the author most likely believes reality television to be",
"shallow",
"corrupt",
"absurd",
"idiotic",
"invaluable")

INSERT INTO QuestionsTable (passage_tablename, question, optionone, optiontwo, optionthree, 
optionfour, optionfive) VALUES 
("Comprehension3", "Which of the following best summarizes the organization of this passage?",
"introduction, history, exposition, conclusion",
"introduction, history, conclusion",
"history, examples, explanations, conclusion",
"exposition, history, conclusion",
"introduction, thesis, supporting paragraphs, conclusion")




























































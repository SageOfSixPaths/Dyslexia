#!/usr/bin/python
# -*- coding: ascii -*-
import database
import MySQLdb
import sys

from pysqlite2 import dbapi2 as sqlite

class Data:
	
	def getWordList(self, exerciseName):
		wordList = []
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			# query string to get the list of words
			queryString = "SELECT word FROM " + exerciseName
			# execute the query
			dbCursor.execute(queryString)
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break 
				wordList.append(row[0])
			return wordList
		except sqlite.OperationalError, msg:
			print(msg)
			sys.exit(1)
			
		dbCursor.close()
		dbConn.close()
	
	def saveNewWordsToDatabase(self, exerciseName, word):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			# query string to get the list of words
			queryFirstPart = "INSERT INTO " + exerciseName + " (word) VALUES ('"
			querySecondPart = ""
			
			querySecondPart = querySecondPart + str(word) + "')"
				
			# The below code removes the extra ",('" 3 characters
			#querySecondPart = querySecondPart[:-3]
			queryString = queryFirstPart + querySecondPart
			# execute the query
			newWordsCount = dbCursor.execute(queryString)
		except sqlite.OperationalError, msg:
			print(msg)
			sys.exit(1)
		
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
		
	def deleteWordsFromDatabase(self, exerciseName, wordList):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			# query string to get the list of words
			queryFirstPart = "DELETE FROM " + exerciseName + " WHERE word IN ('"
			querySecondPart = ""
			
			for word in wordList:
				querySecondPart = querySecondPart + str(word) + "','"
				
			# The below code removes the extra ",('" 3 characters
			querySecondPart = querySecondPart[:-2] + ')'
			queryString = queryFirstPart + querySecondPart
			# execute the query
			deletedRows = dbCursor.execute(queryString)
			#return deletedRows
		except sqlite.OperationalError, msg:
			print(msg)
			sys.exit(1)
		
		dbConn.commit()	
		dbCursor.close()
		dbConn.close()
		
	def updateWordsFromDatabase(self, exerciseName, wordsToUpdateInDatabase, oldWordList):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			# query string to get the list of words
			for index in wordsToUpdateInDatabase.keys():
				oldWord = oldWordList[index]
				newWord = wordsToUpdateInDatabase.get(index)
				queryString = "UPDATE "+ exerciseName +" SET word = '"+str(newWord)+"' WHERE word = '" + str(oldWord) + "'"
				updatedRows = dbCursor.execute(queryString)
				return updatedRows
		except sqlite.OperationalError, msg:
			print(msg)
			sys.exit(1)
			
		dbCursor.close()
		dbConn.close()
	
	def getExerciseList(self):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryString = "SELECT Exercise FROM Exercises"
			dbCursor.execute(queryString)
			exerciseList = []
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break 
				exerciseList.append(row[0])
			return exerciseList
		except sqlite.OperationalError, msg:
			print (msg)
			sys.exit(1)
		
		dbCursor.close()
		dbConn.close()
		
	def addExercise(self, exerciseName, description):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryStringFirstPart = "INSERT INTO Exercises (Exercise, Description) VALUES ("
			
			queryStringSecondPart = "'"+exerciseName+"','"+description+"')"
			queryString = queryStringFirstPart + queryStringSecondPart
			dbCursor.execute(queryString)
		except sqlite.OperationalError, msg:
			print (msg)
			sys.exit(1)
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
			
	def createExerciseTable(self, exerciseName):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryString = "CREATE TABLE " + exerciseName + " (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Word VARCHAR(50))"
			
			dbCursor.execute(queryString)
		except sqlite.OperationalError, msg:
			print (msg)
			sys.exit(1)
		dbConn.commit()
		dbCursor.close()
		dbConn.close() 
			
	def deleteExerciseName(self, exerciseName):
		try:
			# get the connecttion for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryString = "DELETE FROM Exercises WHERE Exercise = '"+exerciseName+"'"
			
			dbCursor.execute(queryString)
		except sqlite.OperationalError, msg:
			print(msg)
			
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
		
	def removeExerciseTable(self, exerciseName):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryString = "DROP TABLE "+exerciseName
			
			dbCursor.execute(queryString)
		except sqlite.OperationalError, msg:
			print(msg)
			
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
	
	def insertSynonmymsToDatabase(self, exerciseName, first_word, second_word):
		try:
			# get the connection for the database
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			# query string to get the list of words
			queryFirstPart = "INSERT INTO " + exerciseName + " (first_word, second_word) VALUES ('"
			querySecondPart = ""
			
			querySecondPart = querySecondPart + str(first_word) +"', '" + str(second_word)+"')"
				
			# The below code removes the extra ",('" 3 characters
			#querySecondPart = querySecondPart[:-3]
			queryString = queryFirstPart + querySecondPart
			# execute the query
			newWordsCount = dbCursor.execute(queryString)
			#return newWordsCount
		except sqlite.OperationalError, msg:
			print(msg)
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
	
	def getSynonymWords(self, tableName):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			query = 'SELECT first_word, second_word FROM '+str(tableName)
			
			masterListWithTwoWords = []
			firstWordList = []
			secondWordList = []
			
			dbCursor.execute(query)
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break
				firstWordList.append(row[0])
				secondWordList.append(row[1])
			
			masterListWithTwoWords.append(firstWordList)
			masterListWithTwoWords.append(secondWordList)
		except sqlite.OperationalError, msg:
			print (msg)
		dbCursor.close()
		dbConn.close()
		return masterListWithTwoWords
	
	def getSentencesFromDatabase(self, tableName, rangeValues):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			query = ('SELECT sentence, optionone, optiontwo,' +
			 'optionthree, optionfour FROM '+ tableName + ' WHERE Id BETWEEN ' 
			 + rangeValues[0] + ' AND '+ rangeValues[1])
			
			masterListWithTwoTypes = []
			sentenceList = []
			wordList = []
			wordMap = {}
			index = 0
			
			dbCursor.execute(query)
			
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break
				sentenceList.append(row[0])
				wordList.append(row[1])
				wordList.append(row[2])
				wordList.append(row[3])
				wordList.append(row[4])
				wordMap[index] = wordList
				wordList = []
				index = index + 1
				
			masterListWithTwoTypes.append(sentenceList)
			masterListWithTwoTypes.append(wordMap)
		except sqlite.OperationalError, msg:
			print (msg)
		
		dbCursor.close()
		dbConn.close()
		return masterListWithTwoTypes
	
	def insertSentenceInTable(self, sentenceText, optionOne, optionTwo, optionThree, optionFour, optionFive):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			## Insert Low Beginnning Level Sentences
			query = ("INSERT INTO LAL_Sentences (sentence, optionone, optiontwo, optionthree, optionfour, optionfive)" +
					"VALUES ('"+sentenceText+"','"+optionOne+"', '"+optionTwo+"', '"+optionThree+"', '"+optionFour+ "','"+optionFive+"')")
			
			dbCursor.execute(query)
		except sqlite.OperationalError, msg:
			print (msg)
			return False

		dbConn.commit()
		dbCursor.close()
		dbConn.close()
		return True	
		
	def deleteSentencesFromDatabase(self, sentenceList):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			queryFirstPart = "DELETE FROM Sentences WHERE sentence IN ('"
			querySecondPart = ''
			
			if len(sentenceList) > 0:
				for sentence in sentenceList:
					querySecondPart = querySecondPart + str(sentence) + "','"
				
				querySecondPart = querySecondPart[:-2] + ')'	
				
				query = queryFirstPart + querySecondPart
				
				dbCursor.execute(query)
		except sqlite.OperationalError, msg:
			print ('Database Error' +str(msg))
		
		dbConn.commit()
		dbCursor.close()
		dbConn.close()
		
	def getCountOfRecords(self, tableName):
		try:
			dbConn = database.Database().getConnection()
			dbCursor  = dbConn.cursor()
			query = "SELECT COUNT(*) FROM "+tableName
			
			countCursor = dbCursor.execute(query)
			rowCount = countCursor.fetchone()[0]
			return rowCount
		except sqlite.OperationalError, msg:
			print ('Database Error' + str(msg))
			
		dbCursor.close()
		dbConn.close()
		
	def getPassageList(self):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			query = "SELECT * FROM Passages"
			
			passageMap = {}
			dbCursor.execute(query)
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break
				passageMap[row[0]] = row[1]
		except sqlite.OperationalError, msg:
			print ('Database Error' + str(msg))
		
		dbCursor.close()
		dbConn.close()
		return passageMap

	def getPassageContent(self, tableName):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			query = "Select passage_content FROM PassageContent where passage_tablename = '"+tableName+"'"
			
			dbCursor.execute(query)
			contentText = ""
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break
				contentText = row[0]	
		except sqlite.OperationalError, msg:
			print ('Database Error' + str(msg))
			
		dbCursor.close()
		dbConn.close()
		return contentText
		
	def insertPassageContent(self, tableName):
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			textContent = 'The word euthanasia is of Greek origin'
			#finalTextContent = textContent.encode('ascii')
			#query = ("INSERT INTO LAL_Sentences (sentence, optionone, optiontwo, optionthree, optionfour, optionfive)" +
			#		"VALUES ('"+sentenceText+"','"+optionOne+"', '"+optionTwo+"', '"+optionThree+"', '"+optionFour+ "','"+optionFive+"')")
		
			query = ("INSERT INTO PassageContent (passage_content, passage_tablename)" +
					"VALUES ('"+textContent+"','"+tableName+"')")
			dbCursor.execute(query)
			
		except sqlite.OperationalError, msg:
			print ('Database Error' + str(msg))
			
		dbCursor.close()
		dbConn.close()
		
	def getQuestionsFromDatabase(self, tableName):
		masterListWithTwoTypes = []
		try:
			dbConn = database.Database().getConnection()
			dbCursor = dbConn.cursor()
			query = ("SELECT question, optionone, optiontwo," +
			 "optionthree, optionfour, optionfive FROM QuestionsTable WHERE passage_tablename = '"+tableName+"'")
			dbCursor.execute(query)
			questionsList = []
			optionsList = []
			optionsMap = {}
			index = 0
			while(1):
				row = dbCursor.fetchone()
				if row == None:
					break
				questionsList.append(row[0])
				optionsList.append(row[1])
				optionsList.append(row[2])
				optionsList.append(row[3])
				optionsList.append(row[4])
				optionsList.append(row[5])
				optionsMap[index] = optionsList
				optionsList = []
				index = index + 1
			
			masterListWithTwoTypes.append(questionsList)
			masterListWithTwoTypes.append(optionsMap)
		except sqlite.OperationalError, msg:
			print ('Database Error' + str(msg))
				
		dbCursor.close()
		dbConn.close()
		return masterListWithTwoTypes

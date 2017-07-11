#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera



def homework():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = 'Mom'
	tear_word = 'abase'

	print '%s is reading an English book.' % (who)
	if not search('etiquette', book, who): 
		tear_mean = book[tear_word]

		del book[tear_word]    
		print "%s tears the page of %s."  % (who, tear_word)

		if search('abase', book, who):
			book[tear_word] = tear_mean
			print '%s adds the page of %s.' % (who, tear_word)


	for key in book:
		if search(key, book, who):
			print '%s finds the meaning of %s: %s.' % (who, key, book[key])



def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s finds the meaning of %s: %s.' % (who, key, dictionary[key])
		return True
	else:
		print '%s does not find %s.' % (who, key)
		return False


if __name__ == '__main__':
	homework()
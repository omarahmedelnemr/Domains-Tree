class Node:
   def __init__(self, dataval,i=0):
      self.dataval = dataval
      self.key = self.dataval+str(i)
      self.keyList = []
      self.childList = []

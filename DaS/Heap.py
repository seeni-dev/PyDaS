"""
	Class definition for heaps min-heap max -heap
"""
"""Methods for getiing parent , left and right nodes"""
import math
def parent(i):
	return math.floor((i-1)/2)
def left(i):
	return 2*i+1
def right(i):
	return 2*i+2
#min-heap in which root node value is smaller than that of its subtrees
class MinHeap():
	"""initializer for min-heap wither with an array or empty one"""
	def __init__(self,array=None):
			if(array==None):
				print("array Needs to passed as argument")
				return;
			self.heap=[]
			self.heapsize=0
			self.create_Heap(array);

	"""method for making heap fro a subarray"""
	def minHeapify(self,i):
		key=self.heap[i]
		l=left(i)
		r=right(i)
		print("in function for {}".format(key))
		while(i<self.heapsize/2):
			minsub=l
			print("i=={} left={} right={}".format(i,l,r))
			print("heap[i]={} left={} right=".format(self.heap[i],self.heap[l]))
			#right child going out of the box
			if( r>(self.heapsize-1) ):
				if(l<self.heapsize and self.heap[l]<key):
					self.heap[i]=self.heap[l]
					i=l
				break;
			if(self.heap[r]<self.heap[l]):
				minsub=r
			if(key>self.heap[minsub]):
				print("exchagning {} with {}".format(self.heap[i],self.heap[minsub]))
				self.heap[i]=self.heap[minsub] 
				i=minsub
				l=left(i)
				r=right(i)
			else:
				break
		self.heap[i]=key

	""""create-heap"""
	def createHeap(self,array):
		self.heap=array
		self.heapsize=len(array)
		for i in range(math.floor(self.heapsize/2),-1,-1):
			print("Calling heap on {}".format(i))
			self.min_heapify(i)

	""" insert method"""
	def insert(n):
		self.heapsize+=1
		self.heap.append(n)
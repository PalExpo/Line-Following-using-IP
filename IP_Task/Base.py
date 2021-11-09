from Motor import *	
GPIO.setmode(GPIO.BCM)					
class Base:

	m_1 = None
	m_2 = None
	m_3 = None
	m_4 = None
	dC = 50													#dC = DutyCycle

	def __init__(self, m_1, m_2, m_3, m_4):
		self.m_1 = m_1
		self.m_2 = m_2
		self.m_3 = m_3
		self.m_4 = m_4

	def forward(self):
		self.m_1.wholeClk(self.dC)
		self.m_2.wholeClk(self.dC)
		self.m_3.wholeAclk(self.dC)
		self.m_4.wholeAclk(self.dC)

	def backward(self):
		self.m_1.wholeAclk(self.dC)
		self.m_2.wholeAclk(self.dC)
		self.m_3.wholeClk(self.dC)
		self.m_4.wholeClk(self.dC)

	def right(self):
		self.m_1.wholeAclk(self.dC)
		self.m_2.wholeClk(self.dC)
		self.m_3.wholeClk(self.dC)
		self.m_4.wholeAclk(self.dC)

	def left(self):
		self.m_1.wholeClk(self.dC)
		self.m_2.wholeAclk(self.dC)
		self.m_3.wholeAclk(self.dC)
		self.m_4.wholeClk(self.dC)

	def upRight(self):
		self.m_1.stopp(self.dC)
		self.m_2.wholeClk(self.dC)
		self.m_3.stopp(self.dC)
		self.m_4.wholeAclk(self.dC)

	def upLeft(self):
		self.m_1.wholeClk(self.dC)
		self.m_2.stopp(self.dC)
		self.m_3.wholeAclk(self.dC)
		self.m_4.stopp(self.dC)

	def downRight(self):
		self.m_1.wholeAclk(self.dC)
		self.m_2.stopp(self.dC)
		self.m_3.wholeClk(self.dC)
		self.m_4.stopp(self.dC)

	def downLeft(self):
		self.m_1.stopp(self.dC)
		self.m_2.wholeAclk(self.dC)
		self.m_3.stopp(self.dC)
		self.m_4.wholeClk(self.dC)

	def clockWise(self):
		self.m_1.wholeAclk(self.dC)
		self.m_2.wholeAclk(self.dC)
		self.m_3.wholeAclk(self.dC)
		self.m_4.wholeAclk(self.dC)

	def antiClockWise(self):
		self.m_1.wholeClk(self.dC)
		self.m_2.wholeClk(self.dC)
		self.m_3.wholeClk(self.dC)
		self.m_4.wholeClk(self.dC)

	def baseStop(self):
		self.m_1.stopp()
		self.m_2.stopp()
		self.m_3.stopp()
		self.m_4.stopp()

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class A(App):
	def build(self):
		self.sound = SoundLoader.load('yoursoundfile.mp3')
		
		return Button(text='play',on_release=self.splay)
	def splay(self,obj):
		if self.sound:
			print("Sound found at %s" % self.sound.source)
			print("Sound is %.3f seconds" % self.sound.length)
			self.sound.play()

A().run()

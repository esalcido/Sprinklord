# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PollsConfig(AppConfig):
	name = 'polls'

	def ready(self):
		print "at polls config."
		from polls.forecastUpdater import updater	
		updater.start()

		#from polls.SprinklerLord import waterSchedule
		#waterSchedule.start()

from controller.add import main as do_add
from controller.edit import main as do_edit
from controller.reindex import main as do_reindex
import shlex


class VonController:
	def do_add(self, argv):
		do_add(argv)
	def do_edit(self, argv):
		do_edit(argv)
	def do_reindex(self, argv):
		do_reindex(argv)
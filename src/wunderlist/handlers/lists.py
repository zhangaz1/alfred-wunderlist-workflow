from wunderlist import util, icons

def _list_name(args):
	return ' '.join(args[1:]).strip()

def filter(args):
	list_name = _list_name(args)
	subtitle = list_name if list_name else 'Type the name of the list'

	util.workflow().add_item('New list...', subtitle, arg=' '.join(args), valid=list_name != '', icon=icons.LIST)

	util.workflow().add_item(
		'Main menu',
		autocomplete='', icon=icons.BACK
	)

def commit(args):
	from wunderlist.api import lists
	from wunderlist.sync import sync

	list_name = _list_name(args)

	lists.create_list(list_name)

	sync()
class FilterModule(object):
    def filters(self):
        return {'makedict': lambda _val: {v['item']['key']: v['stdout'] for v in _val}}
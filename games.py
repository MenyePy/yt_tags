mine = ['gaming', 'games', 'new', 'update', 'minecraft', 'mod', 'youtube', 'livestream', 'HD', 'ps5', 'release', '2021', 'mod', 'dream', 'technoblade', 'gameplay', 'newest version', 'wars', 'smp', 'survival', 'creative', 'top']
fortnite = ['gaming', 'games', 'new', 'update', 'wars', 'victory royale', 'win', 'live', 'fortnite', 'fortnite build', 'fortnite pvp', 'tips', 'fortnite pro', 'fortnite new season', 'fortnite wars', 'livestream', 'youtube', 'HD', '60fps', 'PC']
dls21 = ['soccer',  'dls21', 'Dream League Soccer 2021', 'goal', 'legendary', '15-0', 'online', 'dream league soccer live', 'gameplay', 'high quality', 'HD60FPS', 'youtube', 'new', 'top', 'goals', 'realistic', 'fifa', 'pes', 'fut', 'pes career', 'mobile', 'gameplay']
general = ['youtube',  'top', 'new', 'update', 'gaming', 'mobile', 'pc', 'win', 'gg', 'live', 'online', 'epic', 'mod', 'new release', '2021']

def retrieveTags(game):
    if 'mine' or 'craft' in game:
        return mine
    elif 'fortnite' in game:
        return fortnite
    elif 'dls' in game:
        return dls21
    else:
        return general

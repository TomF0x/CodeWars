# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(sec, rep=""):
    if sec == 0: return 'now'
    years = int(sec / 31536000)
    days = int((sec - (years * 31536000)) / 86400)
    hours = int((sec - (days * 86400) - (years * 31536000)) / 3600)
    minutes = int((sec - (hours * 3600) - (days * 86400) - (years * 31536000)) / 60)
    seconds = sec - (hours * 3600) - (minutes * 60) - (days * 86400) - (years * 31536000)
    if years > 1:
        if len(rep) != 0:
            rep += ', {} years'.format(years)
        else:
            rep += '{} years'.format(years)
    elif years == 1:
        if len(rep) != 0:
            rep += ', 1 year'
        else:
            rep += '1 year'
    if days > 1:
        if len(rep) != 0:
            rep += ', {} days'.format(days)
        else:
            rep += '{} days'.format(days)
    elif days == 1:
        if len(rep) != 0:
            rep += ', 1 day'
        else:
            rep += '1 day'
    if hours > 1:
        if len(rep) != 0:
            rep += ', {} hours'.format(hours)
        else:
            rep += '{} hours'.format(hours)
    elif hours == 1:
        if len(rep) != 0:
            rep += ', 1 hour'
        else:
            rep += '1 hour'
    if minutes > 1 and seconds == 0 and len(rep) != 0:
        if len(rep) != 0:
            rep += ' and {} minutes'.format(minutes)
        else:
            rep += ' and {} minutes'.format(minutes)
    if minutes > 1 and not 'minute' in rep:
        if len(rep) != 0:
            rep += ', {} minutes'.format(minutes)
        else:
            rep += '{} minutes'.format(minutes)
    elif minutes == 1 and seconds == 0:
        if len(rep) != 0:
            rep += ' and 1 minute'
        else:
            rep += ' and 1 minute'
    elif minutes == 1:
        if len(rep) != 0:
            rep += ', 1 minute'
        else:
            rep += '1 minute'
    if seconds > 1:
        if len(rep) != 0:
            rep += ' and {} seconds'.format(seconds)
        else:
            rep += ' and {} seconds'.format(seconds)
    elif seconds == 1:
        if len(rep) != 0:
            rep += ' and 1 second'
        else:
            rep += '1 second'
    return rep

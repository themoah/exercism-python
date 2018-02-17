def hey(args):
    query = args.strip()
    if len(query) == 0:
        return "Fine. Be that way!"
    if query.upper() == query and any(s.isalpha() for s in query):
        return "Whoa, chill out!"
    if query.endswith("?"):
        return "Sure."
    else:
        return "Whatever."

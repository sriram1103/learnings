    match    Match a regular expression pattern to the beginning of a string.
    search   Search a string for the presence of a pattern.
    sub      Substitute occurrences of a pattern found in a string.
    subn     Same as sub, but also return the number of substitutions made.
    split    Split a string by the occurrences of a pattern.
    findall  Find all occurrences of a pattern in a string.
    finditer Return an iterator yielding a match object for each match.
    compile  Compile a pattern into a RegexObject.
    purge    Clear the regular expression cache.
    escape   Backslash all non-alphanumerics in a string.


The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?iLmsux) Set the I, L, M, S, U, or X flag for the RE (see below).
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.        

compile(pattern, flags=0)
    Compile a regular expression pattern, returning a pattern object.

escape(pattern)
    Escape all non-alphanumeric characters in pattern.

findall(pattern, string, flags=0)
    Return a list of all non-overlapping matches in the string.

    If one or more groups are present in the pattern, return a
    list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result.

finditer(pattern, string, flags=0)
    Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a match object.

    Empty matches are included in the result.

match(pattern, string, flags=0)
    Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found.

purge()
    Clear the regular expression cache.
     
search(pattern, string, flags=0)
    Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.

split(pattern, string, maxsplit=0, flags=0)
    Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.

sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.

subn(pattern, repl, string, count=0, flags=0)
    Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the match object and must
    return a replacement string to be used.

template(pattern, flags=0)
    Compile a template pattern, returning a pattern object

m = re.match("^(.+):\s+(.*)$", line.strip())
 m = re.match("^([^:]+):\s+.*UUID=\"([^\"]+)\"\s+TYPE=\"([^\"]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m2 = re.match("UUID=([^\s]+)", theDevice)
 m = re.match("^\s*([^\s\d]+)", line)
 m = re.match("^\s*([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^\s*([^\s]+)\s+([^\s]+)", line)
 theFilesToIgnore.append(file)
 elif re.match(r'^\d*$',theNoOfDaysRetain):
 value = re.findall(r'\d+', str(cacheValue))
 level=logging.DEBUG)
 shutil.copy( "/tmp/restore.log", LOGPATH+"/"+"cfrestore_"+time.strftime("%Y%m%d_%H%M%S")+".log")
 sys.exit("Error during restore. Reason: %s" %(e))
 m = re.match("^([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)", line)
 m = re.match("^([^\s]+)\s+([^\s]+)", line)
 if re.match(".*part\d+$", link):
 if re.match(".*sr\d+$", path):
 line = re.sub("^(UUID=)([^\s]+)", self.replaceUUID, line);
